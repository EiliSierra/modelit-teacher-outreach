# ModelIt! Teacher Outreach - HubSpot Automation

Automated tools for K-12 teacher contact management, email campaigns, and HubSpot CRM integration.

## Overview

Complete campaign system for reaching K-12 teachers to promote ModelIt educational simulations through webinars and TPT sales.

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
├── docs/
│   └── campaign-plan.md      # Complete campaign strategy
├── data/                     # Extracted contact data
│   ├── carlsbad_staff_directory.csv
│   └── carlsbad_staff_directory.xlsx
├── requirements.txt
└── README.md
```

## Campaign Strategy

### Conversion Funnel
```
Email inicial → Registro Webinar → Asistencia → Visita TPT → Compra
```

### Lead Scoring System (Cold/Warm/Hot)

| Score | Status | Action |
|-------|--------|--------|
| 0-10 | **Cold** | Keep in nurture sequence |
| 11-30 | **Warm** | Personalized follow-up email |
| 31-60 | **Hot** | Priority for follow-up |
| 61+ | **Very Hot** | Personal contact / call |

### Email Sequences

**Pre-Webinar (5 emails):**
1. Introduction + demo video
2. Reminder (non-openers)
3. Lead magnet (free PDF guide)
4. Urgency (3 days before)
5. Webinar day (Zoom link)

**Post-Webinar (3 emails):**
6. Thank you + replay + resources
7. Special offer (attendees only)
8. Final follow-up + FAQ

### Visual Materials (Hooks)
- Demo video (2-3 min)
- PDF Lead Magnet: "Systems Thinking Guide for Your Class"
- Webinar replay + slides

## Scripts

### HubSpot Integration

| Script | Description |
|--------|-------------|
| `upload_carlsbad_to_hubspot.py` | Upload Carlsbad USD contacts (342 teachers) |
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

## Tools

- **HubSpot**: CRM and contact lists
- **SendGrid**: Email sending
- **n8n**: Workflow automation
- **Zoom**: Webinars

## Target Metrics

| Metric | Goal |
|--------|------|
| Email open rate | >25% |
| Click rate | >5% |
| Webinar registration | >10% |
| Webinar attendance | >40% |
| TPT visits | >20% |
| Purchase conversion | >5% |

## Documentation

- [Complete Campaign Plan](docs/campaign-plan.md)

## Contact

**Owner**: Eili Sierra

---

*Built with Claude Code*
