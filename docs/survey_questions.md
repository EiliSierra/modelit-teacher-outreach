# Feedback Survey - "From Plug to Steam" Lesson

## Overview

This survey collects feedback from teachers who downloaded the free lesson. The responses are used to segment leads into hot (webinar invite) vs cold (TPT direct) paths.

**Platform:** Google Forms (recommended) or Typeform
**Length:** 2 minutes (7 questions)
**Timing:** Sent 7-10 days after lesson download

---

## Survey Title

**"How was 'From Plug to Steam'?"**

Subtitle: Your feedback helps us create better resources. Takes less than 2 minutes.

---

## Questions

### Question 1: Lesson Usage

**Did you try the lesson with your students?**

Type: Multiple choice (single select)

| Option | Value for Segmentation |
|--------|------------------------|
| Yes, I used the full lesson | `used_full` |
| Yes, but only parts of it | `used_partial` |
| Not yet, but I plan to | `plan_to_use` |
| No, it didn't work for my class | `did_not_use` |

**Logic:**
- If "No, it didn't work" → Skip to Question 4 (improvement suggestions)

---

### Question 2: Overall Rating

**How would you rate the lesson overall?**

Type: Linear scale (1-5 stars)

```
1 ⭐ - Not useful
2 ⭐⭐ - Below expectations
3 ⭐⭐⭐ - Met expectations
4 ⭐⭐⭐⭐ - Above expectations
5 ⭐⭐⭐⭐⭐ - Excellent, would recommend
```

**Segmentation:**
- 4-5 stars → Hot lead → Email 4 (Webinar invite)
- 1-3 stars → Cold lead → Email 5 (TPT resources)

---

### Question 3: What They Liked

**What did you like most?** (Select all that apply)

Type: Checkbox (multiple select)

| Option | Insight |
|--------|---------|
| Easy to set up | Values simplicity |
| Students were engaged | Cares about engagement |
| Clear instructions | Values organization |
| The simulation was effective | Understands ModelIt value |
| Aligned with my curriculum | Standards-focused |
| The video walkthrough was helpful | Uses support materials |
| Other: [text field] | Custom feedback |

---

### Question 4: Improvement Suggestions

**What could be improved?** (Optional)

Type: Long text (paragraph)

Placeholder: "Share any suggestions or challenges you faced..."

**Purpose:** Gather product feedback for future iterations

---

### Question 5: Grade Level

**What grade do you teach?**

Type: Multiple choice (single select)

| Option | Value |
|--------|-------|
| 6th grade | `6` |
| 7th grade | `7` |
| 8th grade | `8` |
| 9th grade | `9` |
| Multiple grades | `multi` |
| Other: [text] | `other` |

---

### Question 6: Topic Interest

**What science topics would you like to see next?** (Select up to 3)

Type: Checkbox (multiple select, max 3)

| Option | Product Development Insight |
|--------|----------------------------|
| Ecosystems / Food webs | High demand topic |
| Chemical reactions | Chemistry curriculum |
| Earth systems / Climate | Environmental science |
| Human body systems | Life science |
| Physics / Forces | Physical science |
| Electricity & circuits | Physical science |
| Genetics / DNA | Life science |
| Other: [text] | Custom ideas |

**Purpose:** Prioritize future lesson development

---

### Question 7: Webinar Interest

**Would you be interested in a free webinar showing more ModelIt lessons?**

Type: Multiple choice (single select)

| Option | Segmentation Action |
|--------|---------------------|
| Yes, I'd love to attend | → Email 4 (immediate webinar invite) |
| Maybe, send me info | → Email 4 (softer invite) |
| No thanks | → Email 5 (TPT direct) |

---

## Hidden Fields (Auto-populated)

These fields should be pre-filled from the survey link using URL parameters:

| Field | Parameter | Example |
|-------|-----------|---------|
| Contact Email | `email` | `?email={{contact.email}}` |
| HubSpot Contact ID | `hs_id` | `?hs_id={{contact.hs_object_id}}` |
| Download Date | `download_date` | `?download_date={{download_date}}` |

**Example Survey Link:**
```
https://forms.gle/XXXXX?email={{contact.email}}&hs_id={{contact.hs_object_id}}
```

---

## Segmentation Rules Based on Responses

### Hot Lead (→ Email 4: Webinar Invite)

Criteria (ANY of the following):
- Question 2 (Rating) = 4 or 5 stars
- Question 7 (Webinar interest) = "Yes, I'd love to attend"

**Action:** Add to list "Survey - Hot Leads", send Email 4

### Warm Lead (→ Email 4: Softer Invite)

Criteria:
- Question 2 (Rating) = 3 stars
- Question 7 (Webinar interest) = "Maybe, send me info"

**Action:** Add to list "Survey - Warm Leads", send Email 4 with softer CTA

### Cold Lead (→ Email 5: TPT Resources)

Criteria (ANY of the following):
- Question 2 (Rating) = 1 or 2 stars
- Question 7 (Webinar interest) = "No thanks"
- Question 1 (Usage) = "No, it didn't work for my class"

**Action:** Add to list "Survey - Cold Leads", send Email 5

### No Response (→ Email 5: TPT Resources)

Criteria:
- Did not complete survey within 5 days of receiving Email 3

**Action:** Add to list "Survey - No Response", send Email 5

---

## Integration with HubSpot

### Option A: Google Forms + Zapier

```
Google Form Submission
    ↓ (Zapier trigger)
Find HubSpot Contact by email
    ↓
Update Contact Properties:
    - survey_completed = true
    - survey_rating = [Q2 value]
    - survey_webinar_interest = [Q7 value]
    ↓
Add to appropriate list based on segmentation rules
```

### Option B: Typeform + Native HubSpot Integration

Typeform has native HubSpot integration that can:
- Create/update contacts automatically
- Map form fields to HubSpot properties
- Trigger workflows based on responses

### Option C: HubSpot Forms (Built-in)

Create the survey directly in HubSpot Forms:
- No integration needed
- Automatic contact property updates
- Native workflow triggers

---

## HubSpot Properties to Update

After survey completion, update these contact properties:

| Property Name | Type | Mapped From |
|---------------|------|-------------|
| `survey_completed` | Boolean | Form submitted = true |
| `survey_date` | Date | Submission timestamp |
| `survey_rating` | Number | Question 2 |
| `survey_lesson_used` | Dropdown | Question 1 |
| `survey_liked_features` | Multi-checkbox | Question 3 |
| `survey_improvement_notes` | Text | Question 4 |
| `survey_grade_taught` | Dropdown | Question 5 |
| `survey_topic_interests` | Multi-checkbox | Question 6 |
| `survey_webinar_interest` | Dropdown | Question 7 |

---

## Thank You Page Content

After submission, redirect to a custom thank you page:

### Thank You Message

```
Thanks for your feedback!

As a thank you, here's early access to our next lesson
(coming soon): "From Sun to Lunch: Energy in Living Systems"

[BUTTON: Join the Early Access List]

In the meantime, explore more lessons in our TPT store:
[LINK: Visit TPT Store]
```

**Purpose:**
- Maintain engagement
- Soft sell TPT store
- Build anticipation for next product

---

## Survey Analytics to Track

| Metric | Target | Calculation |
|--------|--------|-------------|
| Response rate | >40% | Responses / Survey emails sent |
| Average rating | >4.0 | Sum of Q2 / Total responses |
| Hot lead % | >30% | Hot leads / Total responses |
| Webinar interest % | >40% | "Yes" + "Maybe" / Total |
| Completion rate | >90% | Completed / Started |

---

## Sample Google Form Setup

### Form Settings
- [ ] Collect email addresses: ON
- [ ] Limit to 1 response: ON
- [ ] Edit after submit: OFF
- [ ] See summary charts: ON
- [ ] Confirmation message: Custom (see Thank You Page above)

### Response Destination
- Create new spreadsheet: "From Plug to Steam - Survey Responses"
- Connect to Zapier for HubSpot integration

---

## Testing Checklist

Before launching the survey:

- [ ] All questions display correctly
- [ ] Logic jumps work (Q1 "No" → Q4)
- [ ] Hidden fields populate from URL parameters
- [ ] Thank you page displays correctly
- [ ] Responses save to spreadsheet
- [ ] Zapier/integration triggers correctly
- [ ] HubSpot properties update properly
- [ ] Test with your own email first

---

## Files to Create

| File | Platform | Purpose |
|------|----------|---------|
| Google Form | Google Forms | Actual survey |
| Responses Spreadsheet | Google Sheets | Data collection |
| Zapier Zap | Zapier | Google Forms → HubSpot |
| Thank You Page | HubSpot Landing Page | Post-survey redirect |
