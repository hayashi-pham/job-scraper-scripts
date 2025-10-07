# Indeed Job Posting Scraper

A Python script that scrapes Indeed job postings and saves them as self-contained, print-ready HTML files with all styling and images embedded.

## Features

- 🎨 **Preserves Original Styling** - Embeds all CSS stylesheets directly into the HTML
- 🖼️ **Embeds Images** - Converts all images to Base64 data URIs for offline viewing
- 📄 **Print-Ready** - Optimized CSS for clean printing and PDF conversion
- 🔗 **Clickable Logo** - Indeed logo links back to the original job posting
- 🧹 **Clean Output** - Removes unnecessary elements, scripts, and empty divs
- 💾 **Self-Contained** - No internet connection needed to view saved files

## Requirements

- Python 3.7+
- Chrome/Chromium browser
- ChromeDriver (matching your Chrome version)

## Installation

1. **Install required Python packages:**

```bash
pip install selenium beautifulsoup4 requests
```

2. **Install ChromeDriver:**

   **Option A: Direct Download**
   - Download from [ChromeDriver Downloads](https://chromedriver.chromium.org/)
   - Extract and add to your system PATH

   **Option B: Using webdriver-manager (Recommended)**
   ```bash
   pip install webdriver-manager
   ```
   Then modify the script to use:
   ```python
   from webdriver_manager.chrome import ChromeDriverManager
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
   ```

## Usage

### Interactive Mode (Recommended)

Simply run the script and follow the prompts:

```bash
python indeed_scraper.py
```

You'll be asked to enter:
1. The Indeed job URL
2. (Optional) Custom output filename

### Command Line Arguments

**Basic usage:**
```bash
python indeed_scraper.py "https://ca.indeed.com/viewjob?jk=YOUR_JOB_ID"
```

**With custom output filename:**
```bash
python indeed_scraper.py "https://ca.indeed.com/viewjob?jk=YOUR_JOB_ID" "my_job.html"
```

## Examples

**Example 1: Interactive mode**
```bash
$ python indeed_scraper.py
Indeed Job Posting Scraper
--------------------------------------------------
Enter Indeed job URL: https://ca.indeed.com/viewjob?jk=1234567890abcdef
Output filename (press Enter for 'job_posting.html'): software_engineer.html

Loading job posting: https://ca.indeed.com/viewjob?jk=1234567890abcdef
Processing page content...
Embedding CSS stylesheets...
  ✓ Embedded CSS from https://1234567890abcd.cloudfront.net/...
Embedding images as Base64...
  ✓ Embedded 3 images
Removing scripts...
Extracting job posting content...
  ✓ Removed search form
  ✓ Replaced spacing line with logo
  ✓ Removed empty divs
Adding print-friendly styles...
✓ Job posting saved to: software_engineer.html
✓ To convert to PDF, open the HTML file in a browser and use Print > Save as PDF
```

**Example 2: Command line**
```bash
python indeed_scraper.py "https://ca.indeed.com/viewjob?jk=1234567890abcdef" "software_engineer.html"
```

## Converting to PDF

1. Open the generated HTML file in any web browser (Chrome, Firefox, Edge, Safari)
2. Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (Mac)
3. Select "Save as PDF" as the destination
4. Click "Save"

## How It Works

1. **Selenium** loads the Indeed job posting page and waits for content to render
2. **BeautifulSoup** parses the HTML and extracts the job content
3. **CSS Embedding** - Downloads all external stylesheets and converts `<link>` tags to inline `<style>` tags
4. **Image Embedding** - Downloads all images and converts them to Base64 data URIs
5. **Content Extraction** - Extracts only the `jobsearch-ViewJobLayout--standalone` div
6. **Cleanup** - Removes scripts, search forms, and empty divs
7. **Enhancement** - Adds the Indeed logo as a clickable link and includes print-friendly CSS
8. **Output** - Saves a self-contained HTML file ready for viewing or printing

## Output Structure

The saved HTML file contains:
- Indeed logo (clickable, links to original posting)
- Job title and company information
- Job location and type
- Salary information (if available)
- Full job description with original formatting
- All images and styling embedded

## Troubleshooting

**Issue: ChromeDriver version mismatch**
- Solution: Ensure ChromeDriver version matches your Chrome browser version
- Alternative: Use `webdriver-manager` (see Installation section)

**Issue: Timeout waiting for page to load**
- Solution: Increase the wait time in the script:
  ```python
  wait = WebDriverWait(driver, 20)  # Increase from 10 to 20 seconds
  ```

**Issue: "Could not find job posting content"**
- Solution: The page structure may have changed. Check if the class `jobsearch-ViewJobLayout--standalone` still exists
- Try increasing the sleep time: `time.sleep(5)`

**Issue: CSS or images not loading**
- Solution: Check your internet connection
- Some resources may be blocked by corporate firewalls

## Limitations

- Only works with Indeed job postings (URLs containing `indeed.com/viewjob`)
- Requires active internet connection during scraping (for downloading CSS/images)
- May break if Indeed significantly changes their HTML structure
- Some dynamic content loaded via JavaScript may not be captured

## License

This script is provided as-is for personal use. Please respect Indeed's Terms of Service and robots.txt when using this tool.

## Contributing

Feel free to submit issues or pull requests for improvements!

## Disclaimer

This tool is for personal use only. Be respectful of Indeed's servers and don't abuse this script. Always review and comply with Indeed's Terms of Service.
