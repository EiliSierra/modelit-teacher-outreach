# ModelIt! Teacher Outreach - HubSpot Automation

Automated tools for K-12 teacher contact management, email campaigns, and HubSpot CRM integration.

## Overview

Complete campaign system for reaching K-12 teachers to promote ModelIt educational simulations. The campaign uses a **"value-first"** approach: offering a free lesson before asking for commitment to webinars or purchases.

**Target Audience:** 342 teachers from Carlsbad USD
**Free Lesson:** "From Plug to Steam: How Energy Boils Water"
**Goal:** Build trust → Collect feedback → Segment leads → Convert to TPT sales

## Repository Structure

```
modelit-teacher-outreach/
├── scripts/
│   ├── hubspot/                    # HubSpot API integration
│   │   ├── upload_carlsbad_to_hubspot.py
│   │   ├── hubspot_ucla_contacts.py
│   │   └── upload_to_hubspot.py
│   └── scrapers/                   # Web scraping tools
│       └── carlsbad_staff_scraper.py
├── docs/
│   ├── campaign-plan.md            # Complete campaign strategy (v2)
│   ├── email_templates_v2.md       # 8 email templates
│   ├── survey_questions.md         # Feedback survey design
│   ├── lead_scoring.md             # Lead qualification system
│   └── implementation_checklist.md # Step-by-step launch guide
├── data/
│   └── example_contacts.csv        # Example format (no real data)
├── requirements.txt
└── README.md
```

## Campaign Strategy v2

### Conversion Funnel

```
[Free Lesson] → [Feedback Survey] → [Segmentation] → [Webinar/TPT]
```

**Why this works better than direct webinar invites:**
1. **Give value first** — Free lesson builds trust
2. **Qualify leads** — Survey identifies interested teachers
3. **Smart segmentation** — Hot leads → webinar, Cold → TPT direct
4. **Reduce friction** — Only invest time in best prospects

### Email Sequence (8 emails)

| # | Email | Day | Audience |
|---|-------|-----|----------|
| 1 | Free Lesson Offer | 1 | All contacts |
| 2 | Reminder | 3 | Non-downloaders |
| 3 | Feedback Survey | 10 | Downloaders |
| 4 | Webinar Invite | 12 | Hot leads (4-5 stars) |
| 5 | More Resources | 12 | Cold leads / No response |
| 6 | Webinar Replay | 14 | Webinar registrants |
| 7 | Discount Reminder | 17 | Webinar attendees |
| 8 | Final Follow-up | 21 | All engaged contacts |

### Lead Scoring System

| Score | Segment | Action |
|-------|---------|--------|
| 0-15 | **Cold** | Monthly nurture only |
| 16-40 | **Warm** | Value content + soft TPT |
| 41-70 | **Hot** | Webinar invite + promotions |
| 71+ | **Very Hot** | Personal outreach recommended |

### Key Actions & Points

| Action | Points |
|--------|--------|
| Downloaded free lesson | +20 |
| Completed survey | +15 |
| Rating 4-5 stars | +20 to +25 |
| Registered for webinar | +25 |
| Attended webinar | +30 |
| Clicked TPT link | +15 |
| Purchased | +100 |

## Free Lesson Package

**"From Plug to Steam: How Energy Boils Water"**

| Attribute | Value |
|-----------|-------|
| Grade | 8th (adaptable 6-9) |
| Topic | Energy transfer (PS3.A, PS3.B) |
| Duration | ~45 minutes |
| TPT Value | $7.99 → **FREE as sample** |

**Contents:**
- Teacher Guide (PDF)
- Student Activity Pack (printable + digital)
- PowerPoint slides
- Quick Start Guide
- Video walkthrough
- Direct link to ModelIt simulation

## Scripts

### HubSpot Integration

| Script | Description |
|--------|-------------|
| `upload_carlsbad_to_hubspot.py` | Upload Carlsbad USD contacts (342 teachers) |
| `hubspot_ucla_contacts.py` | Upload UCLA Education contacts |
| `upload_to_hubspot.py` | Upload Rhoades School faculty |

### Web Scrapers

| Script | Description |
|--------|-------------|
| `carlsbad_staff_scraper.py` | Extract staff info from 16 Carlsbad USD schools |

## Quick Start

### Prerequisites

```bash
pip install -r requirements.txt
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

- **HubSpot**: CRM, email marketing, workflows
- **Google Forms**: Feedback survey
- **Zapier**: Forms → HubSpot integration
- **Zoom**: Webinars
- **TPT**: Teachers Pay Teachers store

## Target Metrics

| Metric | Goal |
|--------|------|
| Lesson download rate | >30% |
| Survey response rate | >40% |
| Average rating | >4.0 stars |
| Webinar registration (hot leads) | >20% |
| Webinar attendance | >50% |
| TPT visits | >25% |
| Purchase conversion | >5% |

## Documentation

| Document | Description |
|----------|-------------|
| [Campaign Plan](docs/campaign-plan.md) | Complete strategy & funnel |
| [Email Templates](docs/email_templates_v2.md) | All 8 email contents |
| [Survey Questions](docs/survey_questions.md) | Feedback form design |
| [Lead Scoring](docs/lead_scoring.md) | Qualification system |
| [Implementation Checklist](docs/implementation_checklist.md) | Launch guide |

## Data & Privacy

**Real contact data is NOT stored in this repository.**

| Data Type | Location |
|-----------|----------|
| Example/template | `data/example_contacts.csv` (in repo) |
| Real contacts | Local only (never commit) |
| API keys | `.env` file (local only) |

The scraper generates real data locally. Never commit files containing real emails or personal information.

## Contact

**Owner**: Eili Sierra
**TPT Store**: https://www.teacherspayteachers.com/store/modelit

---

*Built with Claude Code | January 2026*
