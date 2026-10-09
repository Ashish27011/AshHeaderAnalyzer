# AshHeaderAnalyzer

AshHeaderAnalyzer is a Python-based HTTP response header analysis tool that collects selected response headers, identifies security-related headers, generates observations, and saves a structured report.

## Features

- HTTP and HTTPS response inspection
- URL validation
- HTTP status and response metadata collection
- General header extraction
- Security header presence checks
- Cookie header detection
- Structured terminal output
- Text report generation

## Headers Inspected

**General headers**
- Server
- Content-Type
- Content-Length
- Location

**Security headers**
- Strict-Transport-Security
- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

**Cookie-related headers**
- Set-Cookie

## Project Architecture

The tool uses separate modules for URL validation, HTTP requests, header extraction, analysis, terminal reporting, and report writing.

```text
User Input
    ↓
URL Validator
    ↓
HTTP Scanner
    ↓
Header Parser
    ↓
Header Analyzer
    ↓
Terminal Reporter
    ↓
Text Report
```

## Requirements

- Python 3
- requests

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AshHeaderAnalyzer.git
cd AshHeaderAnalyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main program:

```bash
python main.py
```

Enter the target URL when prompted.

## Limitations

This is a learning and reconnaissance project. Header presence checks are observations, not proof that a website is secure or vulnerable. The tool does not perform a comprehensive security audit or fully validate header policies.

## Future Improvements

- More detailed header-value analysis
- Cookie security attribute analysis
- Improved redirect handling
- More robust error handling
- Unit tests and structured report formats

## Ethical Use

Use this tool only against systems you own or have explicit permission to assess. Follow applicable laws and the target platform's rules.

## Disclaimer

This project is provided for educational purposes. The user is responsible for ensuring authorized and appropriate use.
