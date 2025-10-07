import time
import base64
import requests
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os

def scrape_indeed_job(url, output_filename="job_posting.html"):
    """
    Scrape an Indeed job posting and save it as a self-contained HTML file
    with embedded CSS and images
    
    Args:
        url: Indeed job posting URL
        output_filename: Output HTML filename
    """
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in background
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    # Headers for downloading resources
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    driver = None
    try:
        # Initialize driver
        driver = webdriver.Chrome(options=chrome_options)
        print(f"Loading job posting: {url}")
        
        # Load the page
        driver.get(url)
        
        # Wait for main content to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "mosaic-aboveViewjobNav")))
        
        # Give extra time for dynamic content
        time.sleep(3)
        
        # Get page source
        html_content = driver.page_source
        
        print("Processing page content...")
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # --- 1. Find, download, and embed CSS stylesheets ---
        print("Embedding CSS stylesheets...")
        for link_tag in soup.find_all('link', {'rel': 'stylesheet'}):
            css_url = urljoin(url, link_tag.get('href', ''))
            if not css_url:
                continue
            try:
                css_response = requests.get(css_url, headers=headers, timeout=10)
                if css_response.status_code == 200:
                    # Create a new <style> tag
                    style_tag = soup.new_tag('style')
                    style_tag.string = css_response.text
                    # Replace the <link> tag with the <style> tag
                    link_tag.replace_with(style_tag)
                    print(f"  ✓ Embedded CSS from {css_url[:60]}...")
            except Exception as e:
                print(f'  ✗ Could not download CSS from {css_url}: {e}')
        
        # --- 2. Find, download, and embed images as Base64 ---
        print("Embedding images as Base64...")
        img_count = 0
        for img_tag in soup.find_all('img'):
            img_url = urljoin(url, img_tag.get('src', ''))
            if not img_url or img_url.startswith('data:'):
                continue
            
            try:
                img_response = requests.get(img_url, headers=headers, timeout=10)
                if img_response.status_code == 200:
                    # Encode image in Base64
                    img_b64 = base64.b64encode(img_response.content).decode('utf-8')
                    # Get the image format
                    img_format = img_url.split('.')[-1].split('?')[0].lower()
                    if 'svg' in img_format:
                        img_format = 'svg+xml'
                    elif 'jpg' in img_format:
                        img_format = 'jpeg'
                    elif img_format not in ['png', 'gif', 'webp', 'bmp']:
                        img_format = 'png'  # default
                    
                    # Replace image src with the Base64 data URI
                    img_tag['src'] = f'data:image/{img_format};base64,{img_b64}'
                    img_count += 1
            except Exception as e:
                print(f'  ✗ Could not download image from {img_url}: {e}')
        
        print(f"  ✓ Embedded {img_count} images")
        
        # --- 3. Remove script tags to prevent dynamic content loading issues ---
        print("Removing scripts...")
        for script_tag in soup.find_all('script'):
            script_tag.decompose()
        
        # --- 4. Extract only the job posting content ---
        print("Extracting job posting content...")
        job_layout = soup.find('div', class_='jobsearch-ViewJobLayout--standalone')
        
        if not job_layout:
            print("✗ Could not find job posting content")
            return None
        
        # Remove the search form div
        search_form = job_layout.find('div', class_=lambda x: x and 'form' in str(x).lower())
        if not search_form:
            search_form = job_layout.find('form', action='/jobs')
        if search_form:
            search_form.decompose()
            print("  ✓ Removed search form")
        
        # Replace the spacing line div with logo
        spacing_line = job_layout.find('div', id='jobsearch-ViewJobLayout-rowSpacingLine')
        logo_div = soup.find('div', class_='gnav-Logo-icon')
        
        if spacing_line and logo_div:
            # Make the logo SVG a clickable link
            svg = logo_div.find('svg')
            if svg:
                # Create an anchor tag
                link = soup.new_tag('a', href=driver.current_url, target='_blank')
                # Wrap the SVG in the link
                svg.wrap(link)
            
            spacing_line.replace_with(logo_div.extract())
            print("  ✓ Replaced spacing line with logo")
        
        # Remove empty divs inside job_layout
        for div in job_layout.find_all('div'):
            # Check if div is empty (no text content and no child elements with content)
            if not div.get_text(strip=True) and not div.find_all(['img', 'svg', 'input', 'button']):
                div.decompose()
        print("  ✓ Removed empty divs")
        
        # Create new minimal HTML with just the job content
        new_soup = BeautifulSoup('<!DOCTYPE html><html><head></head><body></body></html>', 'html.parser')
        
        # Copy head elements (meta, title, styles)
        if soup.head:
            for tag in soup.head.find_all(['meta', 'title', 'style']):
                new_soup.head.append(tag.extract())
        
        # Add the job layout content to body
        new_soup.body.append(job_layout.extract())
        
        soup = new_soup
        
        # --- 5. Add print-friendly CSS ---
        print("Adding print-friendly styles...")
        print_style = soup.new_tag('style')
        print_style.string = """
        @media print {
            body { margin: 0; padding: 20px; }
            .no-print, nav, header, footer, .css-kyg8or, .css-1m4cuuf { 
                display: none !important; 
            }
        }
        body {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .gnav-Logo-icon svg {
            height: 1.75rem;
            width: 7rem;
        }
        .jobsearch-InfoHeaderContainer {
            margin-inline-start: 0 !important;
        }
        @page {
            margin: 1cm;
        }
        """
        if soup.head:
            soup.head.append(print_style)
        
        # --- 5. Save the modified HTML to a file ---
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))
        
        print(f"✓ Job posting saved to: {output_filename}")
        print(f"✓ To convert to PDF, open the HTML file in a browser and use Print > Save as PDF")
        
        return output_filename
        
    except Exception as e:
        print(f"✗ Error scraping job posting: {str(e)}")
        import traceback
        traceback.print_exc()
        return None
        
    finally:
        if driver:
            driver.quit()

# Example usage
if __name__ == "__main__":
    import sys
    
    # Check if URL provided as command line argument
    if len(sys.argv) > 1:
        job_url = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "job_posting.html"
    else:
        # Prompt user for URL
        print("Indeed Job Posting Scraper")
        print("-" * 50)
        job_url = input("Enter Indeed job URL: ").strip()
        
        if not job_url:
            print("✗ No URL provided. Exiting.")
            sys.exit(1)
        
        # Optional: ask for custom filename
        custom_name = input("Output filename (press Enter for 'job_posting.html'): ").strip()
        output_file = custom_name if custom_name else "job_posting.html"
        
        # Ensure .html extension
        if not output_file.endswith('.html'):
            output_file += '.html'
    
    print()
    
    # Scrape and save
    output_file = scrape_indeed_job(job_url, output_file)
    
    if output_file:
        print(f"\n✓ File saved successfully! Open '{output_file}' in your browser to view or print.")
        print("✓ To create a PDF: Open the HTML file → Press Ctrl+P (Cmd+P on Mac) → Save as PDF")