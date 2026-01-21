# Lead Scoring System - ModelIt Teacher Outreach

## Overview

This document defines the lead scoring system used to qualify and prioritize teacher contacts based on their engagement with the campaign.

**Purpose:** Automatically identify which leads are most likely to convert and route them to the appropriate follow-up sequence.

---

## Scoring Model

### Action-Based Points

| Action | Points | Category |
|--------|--------|----------|
| Opened email | +5 | Engagement |
| Clicked any email link | +10 | Engagement |
| Downloaded free lesson | +20 | Interest |
| Completed feedback survey | +15 | Engagement |
| Survey rating 5 stars | +25 | Satisfaction |
| Survey rating 4 stars | +20 | Satisfaction |
| Survey rating 3 stars | +5 | Satisfaction |
| Survey rating 2 stars | -5 | Satisfaction |
| Survey rating 1 star | -10 | Satisfaction |
| Webinar interest = "Yes" | +15 | Intent |
| Webinar interest = "Maybe" | +5 | Intent |
| Webinar interest = "No" | -5 | Intent |
| Registered for webinar | +25 | Intent |
| Attended webinar | +30 | Commitment |
| Watched webinar replay | +15 | Engagement |
| Clicked TPT store link | +15 | Purchase Intent |
| Visited TPT more than once | +20 | Purchase Intent |
| Used discount code | +25 | Purchase Intent |
| Purchased on TPT | +100 | Conversion |

### Decay Rules

To keep scores relevant, apply decay for inactivity:

| Inactivity Period | Decay |
|-------------------|-------|
| 30 days no engagement | -10 points |
| 60 days no engagement | -20 points |
| 90 days no engagement | -30 points |

**Note:** Decay is capped - score cannot go below 0.

---

## Lead Segments

### Segment Definitions

| Score Range | Segment | Description |
|-------------|---------|-------------|
| 0-15 | **Cold** | Minimal engagement, low priority |
| 16-40 | **Warm** | Some interest, needs nurturing |
| 41-70 | **Hot** | High engagement, ready for conversion |
| 71+ | **Very Hot** | Highly qualified, prioritize personal outreach |

### Segment Actions

#### Cold Leads (0-15 points)

**Characteristics:**
- Did not download lesson, OR
- Downloaded but no further engagement, OR
- Low survey rating (1-2 stars)

**Automated Actions:**
- Add to monthly nurture sequence
- Send occasional value content
- Do NOT invite to webinar (waste of effort)
- Soft TPT promotion only

**Manual Actions:**
- No personal outreach required
- Monitor for score increases

---

#### Warm Leads (16-40 points)

**Characteristics:**
- Downloaded lesson
- Some email engagement
- Survey rating 3 stars
- "Maybe" interested in webinar

**Automated Actions:**
- Include in Email 5 (TPT resources)
- Send webinar invite (soft CTA)
- Regular value content

**Manual Actions:**
- Review feedback for insights
- Consider personalized follow-up if score approaching 40

---

#### Hot Leads (41-70 points)

**Characteristics:**
- Downloaded lesson
- High survey rating (4-5 stars)
- "Yes" interested in webinar
- Multiple email opens/clicks

**Automated Actions:**
- Priority webinar invitation (Email 4)
- Discount offers
- TPT promotions

**Manual Actions:**
- Review their survey feedback
- Personalized email if appropriate
- Track webinar registration closely

---

#### Very Hot Leads (71+ points)

**Characteristics:**
- Attended webinar
- Visited TPT multiple times
- Used discount code
- High engagement across all touchpoints

**Automated Actions:**
- Immediate discount reminder
- VIP content access
- Early access to new products

**Manual Actions:**
- **Personal outreach recommended**
- Offer 1-on-1 demo call
- Consider phone follow-up
- Ask for referrals/testimonials

---

## Score Calculation Examples

### Example 1: Highly Engaged Teacher

| Action | Points | Running Total |
|--------|--------|---------------|
| Opened Email 1 | +5 | 5 |
| Clicked download link | +10 | 15 |
| Downloaded lesson | +20 | 35 |
| Opened Email 3 | +5 | 40 |
| Completed survey | +15 | 55 |
| Rated 5 stars | +25 | 80 |
| Webinar = "Yes" | +15 | 95 |
| Registered webinar | +25 | 120 |
| Attended webinar | +30 | 150 |
| Clicked TPT link | +15 | 165 |

**Final Score: 165 (Very Hot)**
**Action:** Personal follow-up recommended

---

### Example 2: Moderately Engaged Teacher

| Action | Points | Running Total |
|--------|--------|---------------|
| Opened Email 1 | +5 | 5 |
| Clicked download link | +10 | 15 |
| Downloaded lesson | +20 | 35 |
| Opened Email 3 | +5 | 40 |
| Completed survey | +15 | 55 |
| Rated 3 stars | +5 | 60 |
| Webinar = "Maybe" | +5 | 65 |

**Final Score: 65 (Hot)**
**Action:** Webinar invite + TPT promotion

---

### Example 3: Low Engagement Teacher

| Action | Points | Running Total |
|--------|--------|---------------|
| Opened Email 1 | +5 | 5 |
| No click | - | 5 |
| Opened Email 2 | +5 | 10 |
| No click | - | 10 |
| No survey | - | 10 |

**Final Score: 10 (Cold)**
**Action:** Monthly nurture only

---

### Example 4: Dissatisfied Teacher

| Action | Points | Running Total |
|--------|--------|---------------|
| Opened Email 1 | +5 | 5 |
| Downloaded lesson | +20 | 25 |
| Completed survey | +15 | 40 |
| Rated 1 star | -10 | 30 |
| Webinar = "No" | -5 | 25 |

**Final Score: 25 (Warm)**
**Action:** Review feedback, soft nurture, improve product based on feedback

---

## HubSpot Implementation

### Contact Property

Create a calculated property called `lead_score`:

| Property | Value |
|----------|-------|
| Name | `lead_score` |
| Label | Lead Score |
| Type | Calculation |
| Field type | Number |

### Workflow: Score Update Triggers

Create workflows that update the score when actions occur:

**Workflow 1: Email Opens**
```
Trigger: Any marketing email opened
Action: Increase lead_score by 5
```

**Workflow 2: Email Clicks**
```
Trigger: Any marketing email link clicked
Action: Increase lead_score by 10
```

**Workflow 3: Lesson Downloaded**
```
Trigger: downloaded_lesson = true
Action: Increase lead_score by 20
```

**Workflow 4: Survey Completed**
```
Trigger: survey_completed = true
Action: Increase lead_score by 15

Branch: If survey_rating = 5
  → Increase lead_score by 25
Branch: If survey_rating = 4
  → Increase lead_score by 20
Branch: If survey_rating = 3
  → Increase lead_score by 5
Branch: If survey_rating = 2
  → Decrease lead_score by 5
Branch: If survey_rating = 1
  → Decrease lead_score by 10
```

**Workflow 5: Webinar Interest**
```
Trigger: survey_webinar_interest is known
Branch: If = "yes"
  → Increase lead_score by 15
Branch: If = "maybe"
  → Increase lead_score by 5
Branch: If = "no"
  → Decrease lead_score by 5
```

**Workflow 6: Webinar Registration**
```
Trigger: webinar_registered = true
Action: Increase lead_score by 25
```

**Workflow 7: Webinar Attendance**
```
Trigger: webinar_attended = true
Action: Increase lead_score by 30
```

**Workflow 8: TPT Click**
```
Trigger: Page view contains "teacherspayteachers.com/store/modelit"
Action:
  - Set tpt_clicked = true
  - Increase lead_score by 15
```

**Workflow 9: Purchase**
```
Trigger: purchased_tpt = true
Action: Increase lead_score by 100
```

### Lists Based on Score

Create smart lists for each segment:

| List Name | Criteria |
|-----------|----------|
| Leads - Cold | lead_score <= 15 |
| Leads - Warm | lead_score > 15 AND lead_score <= 40 |
| Leads - Hot | lead_score > 40 AND lead_score <= 70 |
| Leads - Very Hot | lead_score > 70 |

---

## Reporting Dashboard

### Key Metrics to Track

| Metric | Formula | Target |
|--------|---------|--------|
| Average Lead Score | Sum(scores) / Count(contacts) | >30 |
| Hot Lead % | Hot+VeryHot / Total | >25% |
| Score Progression | Avg score increase per week | +5 |
| Conversion by Score | Purchases per segment | VeryHot >20% |

### Segment Distribution

Track weekly distribution across segments:

```
Week 1: Cold: 70% | Warm: 20% | Hot: 8% | VeryHot: 2%
Week 2: Cold: 60% | Warm: 25% | Hot: 12% | VeryHot: 3%
Week 3: Cold: 50% | Warm: 28% | Hot: 17% | VeryHot: 5%
```

**Goal:** Progressively move contacts up the funnel.

---

## Optimization Guidelines

### When to Review Scoring Model

1. **Monthly:** Check if segment distribution makes sense
2. **After 100 contacts scored:** Validate against actual conversions
3. **When conversion rates change:** Adjust point values

### Tuning Point Values

If too many leads are "Hot" but not converting:
- Increase threshold for Hot (e.g., 50-80 instead of 41-70)
- Reduce points for low-commitment actions

If too few leads are "Hot":
- Decrease threshold
- Increase points for key actions

### A/B Testing Scoring

Consider testing different models:
- **Model A:** Current model
- **Model B:** Higher weight on survey rating
- **Model C:** Higher weight on webinar attendance

Compare conversion rates after 1 month.

---

## Integration with Sales Process

### Notification Triggers

| Event | Notification |
|-------|--------------|
| Lead reaches 70+ points | Slack notification / Email alert |
| Lead attends webinar | Add to "Personal Follow-up" task |
| Lead visits TPT 3+ times | Sales priority flag |

### Handoff to Personal Outreach

When a lead scores 71+:

1. Automatic notification to sales/owner
2. Review contact history in HubSpot
3. Check survey feedback for personalization
4. Send personalized email or schedule call
5. Log outcome in HubSpot

---

## Score Reset Scenarios

### When to Reset Score

| Scenario | Action |
|----------|--------|
| Contact unsubscribed | Set score to 0 |
| Hard bounce | Remove from lists |
| Purchased | Keep score, move to "Customer" pipeline |
| Requested removal | Delete contact |

---

## Summary

**Lead Scoring Benefits:**
1. Prioritize high-value leads automatically
2. Route leads to appropriate sequences
3. Focus manual effort on best prospects
4. Track campaign effectiveness over time
5. Improve conversion rates with targeted outreach

**Key Thresholds:**
- **0-15:** Cold → Monthly nurture
- **16-40:** Warm → Value content + soft sell
- **41-70:** Hot → Webinar + promotions
- **71+:** Very Hot → Personal outreach

**HubSpot Properties Needed:**
- `lead_score` (Number, calculated)
- `downloaded_lesson` (Boolean)
- `survey_rating` (Number)
- `survey_webinar_interest` (Dropdown)
- `webinar_registered` (Boolean)
- `webinar_attended` (Boolean)
- `tpt_clicked` (Boolean)
- `purchased_tpt` (Boolean)
