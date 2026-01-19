# ModelIt! Teacher Outreach - HubSpot Automation

Automated tools for K-12 teacher contact management and HubSpot CRM integration.

## Overview

Scripts for extracting teacher contact information from school districts and uploading to HubSpot CRM for educational outreach campaigns.

## Repository Structure

```
modelit-teacher-outreach/
├── scripts/
│   ├── hubspot/              # HubSpot API integration
│   │   ├── upload_carlsbad_to_hubspot.py
│   │   ├── hubspot_ucla_contacts.py
│   │   └── upload_to_hubspot.py
│   └── scrapers/             # Web scraping tools
│       └── carlsbad_staff_scraper.py
├── data/                     # Extracted contact data
│   ├── carlsbad_staff_directory.csv
│   └── carlsbad_staff_directory.xlsx
├── requirements.txt
└── README.md
```

## Scripts

### HubSpot Integration

| Script | Description |
|--------|-------------|
| `upload_carlsbad_to_hubspot.py` | Upload Carlsbad USD contacts (342 teachers) to HubSpot |
| `hubspot_ucla_contacts.py` | Upload UCLA Education Department contacts |
| `upload_to_hubspot.py` | Upload Rhoades School faculty contacts |

### Web Scrapers

| Script | Description |
|--------|-------------|
| `carlsbad_staff_scraper.py` | Extract staff info from 16 Carlsbad USD schools |

## Quick Start

### Prerequisites

```bash
pip install requests python-dotenv pandas openpyxl beautifulsoup4 lxml
```

### Environment Setup

Create `.env` file:

```env
HUBSPOT_API_KEY=your_hubspot_api_key_here
```

### Usage

**1. Scrape teacher contacts:**
```bash
python scripts/scrapers/carlsbad_staff_scraper.py
```

**2. Upload to HubSpot:**
```bash
python scripts/hubspot/upload_carlsbad_to_hubspot.py
```

## Data Collected

- **Carlsbad USD**: 342 staff contacts from 16 schools
- **UCLA Education**: 4 department chairs
- **Rhoades School**: 20 faculty members

## Contact

**Owner**: Eili Sierra

---

*Built with Claude Code*
