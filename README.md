# ModelIt! Teacher Outreach Automation

Automated tools for K-12 teacher engagement, contact management, and educational marketing campaigns.

## Overview

This repository contains automation tools for reaching K-12 teachers, health educators, and science facilitators to promote **ModelIt!** - an educational simulation platform by Discovery Collective that adapts research-grade modeling technology into engaging science lessons.

## Features

- **HubSpot Integration**: Automated contact upload and CRM management
- **Web Scraping**: Extract teacher contact information from school district websites
- **Email Automation**: Sequences for webinars, onboarding, and nurturing campaigns
- **Multi-platform Outreach**: Tools for reaching teachers across multiple channels

## Repository Structure

```
modelit-teacher-outreach/
├── scripts/
│   ├── hubspot/           # HubSpot API integration scripts
│   │   ├── upload_carlsbad_to_hubspot.py
│   │   ├── hubspot_ucla_contacts.py
│   │   └── upload_to_hubspot.py
│   └── scrapers/          # Web scraping tools
│       └── carlsbad_staff_scraper.py
├── docs/                  # Documentation and plans
│   ├── 01-MASTER-AUTOMATION-PLAN.md
│   ├── 02-IMPLEMENTATION-TIMELINE.md
│   └── 03-COST-ANALYSIS.md
├── data/                  # Extracted contact data (CSV/Excel)
├── workflows/             # n8n automation workflows
└── README.md
```

## Quick Start

### Prerequisites

- Python 3.11+
- HubSpot API Key
- Required Python packages:

```bash
pip install requests python-dotenv pandas openpyxl beautifulsoup4 lxml
```

### Environment Setup

Create a `.env` file in your working directory:

```env
HUBSPOT_API_KEY=your_hubspot_api_key_here
```

### Usage

#### 1. Scrape Teacher Contacts (Carlsbad USD)

```bash
python scripts/scrapers/carlsbad_staff_scraper.py
```

This extracts contact information from 16 schools in Carlsbad Unified School District.

#### 2. Upload to HubSpot

```bash
python scripts/hubspot/upload_carlsbad_to_hubspot.py
```

Uploads scraped contacts to HubSpot CRM with proper tagging.

## Target Audiences

| Audience | Description | Strategy |
|----------|-------------|----------|
| K-12 Science Teachers | Primary target | Webinars, TPT, conferences |
| Health Educators | Secondary | Disease modeling focus |
| Homeschool Parents | Growing segment | Community building |
| Museum/Informal Ed | Partnerships | Special programs |

## Automation Stack

- **CRM**: HubSpot (contact management)
- **Email**: SendGrid (transactional & marketing)
- **Workflows**: n8n (self-hosted automation)
- **Social**: Ayrshare API (multi-platform posting)
- **Analytics**: Google Analytics 4 + custom dashboards

## Key Metrics

- **Webinar attendance rate target**: 60%+
- **Email open rate target**: 25%+
- **Pilot signup conversion**: 10-15%
- **Teacher database goal**: 5,000 by Q4 2025

## Documentation

- [Master Automation Plan](docs/01-MASTER-AUTOMATION-PLAN.md) - Complete technical strategy
- [Implementation Timeline](docs/02-IMPLEMENTATION-TIMELINE.md) - Phased rollout
- [Cost Analysis](docs/03-COST-ANALYSIS.md) - Budget and ROI projections

## Security Notes

- Never commit `.env` files with API keys
- Contact data (CSV/Excel) should be handled according to privacy policies
- Use environment variables for all sensitive credentials

## License

MIT License - For educational purposes.

## Contact

- **Project Lead**: Eili Sierra
- **Organization**: Discovery Collective / Alexandria's Design
- **Related**: [ModelIt! Educational Simulations](https://modelit.com)

---

*Built with Claude Code*
