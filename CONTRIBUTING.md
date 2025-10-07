# Contributing to Job Scraper Scripts — Offline Job Description Archiver

Thanks for helping improve this project! This guide explains how to propose changes, add new scrapers, and keep contributions safe and compliant.

**Hard rules (non-negotiable):**
- **Do not commit any personal data (PII) or scraped output artifacts** (HTML, CSV, JSON, PDFs, logs, screenshots, etc.).
- **Repeated low-value or spammy PRs will be closed** and the accounts **may be banned** from contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [When Adding a New Scraper](#when-adding-a-new-scraper)
- [Contribution Guidelines](#contribution-guidelines)
- [Absolute No-Go: Data, Secrets & Output Artifacts](#absolute-no-go-data-secrets--output-artifacts)
- [Spam & Low-Value PRs](#spam--low-value-prs)
- [Project Structure & Where Things Go](#project-structure--where-things-go)
- [Development Standards](#development-standards)
- [Pull Request Checklist](#pull-request-checklist)
- [Legal & Ethical Scraping](#legal--ethical-scraping)
- [Security & Responsible Disclosure](#security--responsible-disclosure)
- [License](#license)

## Code of Conduct

Be kind, constructive, and professional. Harassment or discrimination is not tolerated. We generally follow the spirit of the Contributor Covenant.

## When Adding a New Scraper

1. **Create a new folder** at the repo root (e.g., `/source/`).

2. **Add your script(s)** and a **`README.md`** that documents:
   - **Prerequisites** (language/runtime & versions)
   - **Installation** steps (dependencies)
   - **Configuration** (env vars, cookies/auth, rate limits)
   - **Usage & options**
   - **Output file naming & location**
   - **Known limitations**

3. **Follow conventions:**
   - Output a **single-file page** (inline assets).
   - Include basic **metadata** in the page where possible.
   - Respect **polite crawling practices** (delays, retries).

4. **Open a PR** with a concise description and **example outputs**.
   - Provide **screenshots** or **synthetic/redacted sample files** **attached to the PR description** (do **not** commit artifacts to the repo).

### **New Scraper PR Checklist**

- [ ] New top-level folder (e.g., `/source/`) with code
- [ ] Thorough `README.md` for that source
- [ ] Produces **single-file HTML** with inline assets
- [ ] Polite crawling (delays/retries) implemented
- [ ] No PII, secrets, or output artifacts committed
- [ ] Screenshots/synthetic samples attached in PR description only

## Contribution Guidelines

We welcome issues and pull requests! To keep things tidy:

### Before you start

- **Open an issue** to discuss substantial changes or new sources.
- Confirm the source’s **Terms of Service** allow what you intend (see [Legal](#legal--ethical-scraping)).

### Code style

- **Python:** PEP 8; type hints where reasonable.
- **JavaScript/TypeScript:** Prettier + ESLint (default configs are fine).
- Keep scripts focused and well-commented; prefer small, testable functions.

### Docs

- Each scraper **must** have its own `README.md` with clear, step-by-step setup and usage.
- Document required **environment variables** and any sensitive configuration (cookies, tokens) without exposing secrets.

### Testing

- Where feasible, include minimal **smoke tests** or a **dry-run mode**.
- Add **sample output** that is **synthetic or fully redacted**; attach examples to the PR description rather than committing artifacts.

### Pull Requests

- Reference related issues.
- Describe the source, approach, and any trade-offs or limitations.
- Note rate-limiting strategy and how retries/backoff are handled.

## Absolute No-Go: Data, Secrets & Output Artifacts

Never commit:

- **Personal data (PII)** or sensitive information of any individual
- **Scraped output** (single-file HTML, screenshots, PDFs, CSV/JSON/NDJSON, etc.)
- **Credentials or secrets**, including cookies, tokens, API keys, session data
- **Logs** containing URLs, identifiers, or anything user-specific

Recommended `.gitignore` entries:

```
# Never commit scraped artifacts or secrets
output/
artifacts/
*.html
*.pdf
*.csv
*.json
*.ndjson
*.log
.env
.env.*
__pycache__/
node_modules/
```

Use **synthetic** or **heavily anonymized** fixtures for examples/tests. If you must show real-world structure, redact fully and attach as images in the PR description (not committed).

## Spam & Low-Value PRs

Please **do not open PRs** that only:

- Fix trivial grammar/spacing in the **root** `README.md`
- Reformat markdown without improving clarity/accuracy
- Rename files without purpose, or break links

Such PRs will be closed. **Repeated spam will lead to a ban from contributing.**
Substantial documentation updates **inside a scraper’s own `README.md`** (e.g., setup changes, auth flow clarifications) are welcome.

## Project Structure & Where Things Go

- Each source lives in its own folder (e.g., `linkedin/`, `indeed/`, `glassdoor/`), with:
  - The scraper code
  - A **source-specific `README.md`** (setup, configuration, usage, limitations)
- The root `README.md` provides the project overview and links to sub-READMEs.
- Shared utilities may live under a future `common/` folder if/when they emerge.

## Development Standards

**Formatting & linting**

- **Python:** Black (format), Ruff/Flake8 (lint)
- **JavaScript/TypeScript:** Prettier (format), ESLint (lint)

**Commits**

- Use clear messages; Conventional Commits (`feat:`, `fix:`, `docs:`, etc.) appreciated.

## Pull Request Checklist

- [ ] Meaningful change (not a trivial root `README.md` touch-up)
- [ ] No PII, secrets, or output artifacts committed
- [ ] Code formatted & linted
- [ ] Tests/fixtures updated or added (synthetic/redacted only)
- [ ] Source-specific `README.md` updated
- [ ] Clear description, with screenshots/synthetic samples attached in PR description

## Legal & Ethical Scraping

By contributing, you agree to:

- **Review and comply** with each site’s ToS and robots.txt
- Respect authentication, rate limits, and access controls
- Avoid collecting/including personal data
- Use and distribute this code **only** for lawful purposes

Contributions that encourage or enable policy violations will be declined.

## Security & Responsible Disclosure

If you believe you’ve found a security issue, please use GitHub **Security Advisories** or open a private report. Do **not** include sensitive details in public issues.

## License

By contributing, you agree your contributions will be licensed under **the MIT Open Source License** (see `LICENSE`).

**Thank you for keeping this project useful, safe, and respectful.**
