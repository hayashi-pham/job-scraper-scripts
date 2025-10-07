# Job Scraper Scripts — Offline Job Description Archiver

Fetch job postings from major job boards (e.g., LinkedIn, Indeed,...), then save each posting as a **single-file web page** for clean printing and reliable offline viewing.

Each scraper produces a self-contained page (e.g., an HTML file with inlined assets) that preserves the source layout as closely as possible and can be viewed on any device without an internet connection.

## Table of Contents

- [Overview](#overview)
- [Supported Sources](#supported-sources)
- [Output Format](#output-format)
- [Prerequisites](#prerequisites)
- [Contributing](#contributing)
- [Legal & Ethical Use](#legal--ethical-use)
- [Roadmap](#roadmap)
- [License](#license)

## Overview

- **Scrapes job descriptions** from supported platforms.
- **Normalizes and saves** each posting as a **self-contained HTML file** (all assets inlined) designed to:
  - Print nicely with minimal clutter.
  - Open offline without broken images, fonts, or styles.
- Keeps each scraper isolated so you can add new sources or languages without affecting others.

Typical use cases:

- Archive postings for offline review.
- Create uniform, printable job description files for sourcing, screening, or research.
- Enable simple downstream processing without juggling multiple assets.

## Supported Sources

- **Indeed** — (see [`indeed/README.md`](indeed/README.md))

## Output Format

- Each job is saved as a **single, portable HTML file** (no external dependencies).
- Files are intended to:
  - **Print** cleanly (print-optimized CSS).
  - **Work offline** (assets inlined).

## Prerequisites

- **Git** - for cloning and version control.
- **Per-scraper runtimes**:
  - Indeed: **Python** - (see [`indeed/README.md`](indeed/README.md))
To keep commands accurate for each language and platform, **all run/setup instructions live in the scraper-specific READMEs**:

## Contributing

We welcome fixes, features, and new scrapers!

1. **Open an issue** describing the change (bug, enhancement, new source).
2. **Fork** → create a feature branch → commit with clear messages.
3. **Add/Update docs**:
   - Each scraper must have its own `README.md` with setup, configuration, and usage.
   - Document environment variables and output paths.
4. **Testing**:
   - If live tests are necessary, gate them behind opt-in flags.
5. **Pull Request**:
   - Link the issue it closes.
   - Provide a short demo (screenshots of output files or sample artifacts).
   - Note any breaking changes or new env vars.

Please refer to [`CONTRIBUTING.md`](CONTRIBUTING.md) for more details.

## Legal & Ethical Use

Scraping may be restricted by a site’s **Terms of Service**, **robots.txt**, **rate limits**, and **local laws**. By using this project, you agree to:

- **Review and comply with each site’s policies** before scraping.
- **Respect authentication, rate limits, and access controls**.
- **Avoid collecting personal data** beyond what is necessary.
- **Use responsibly** and only for lawful purposes.

The maintainers are **not responsible** for misuse or policy violations.

## Roadmap

- [ ] More sources (Glassdoor, company career pages)
- [ ] Shared utilities (normalization, deduping, date parsing)
- [ ] Configurable output templates & themes
- [ ] Optional metadata export (CSV/JSON alongside HTML)
- [ ] Basic test fixtures for stability

## License

This project is licensed under the MIT Open Source License (see `LICENSE`).

### Maintainers / Contact

- **Maintainers**: Lam Pham
- Please open an **Issue** for bugs and feature requests.
- Use **Discussions** (if enabled) for general questions and collaboration.
