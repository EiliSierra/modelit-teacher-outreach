# Feedback Survey - "From Plug to Steam" Lesson

## Overview

This survey collects honest feedback from teachers who viewed the free lesson on Google Drive. Responses help improve future lessons and identify teachers interested in the webinar.

**Platform:** Google Forms (recommended)
**Length:** 2 minutes (8 questions)
**Timing:** Sent 5-7 days after viewing lesson
**Incentive:** $5 Starbucks gift card (mentioned in email, NOT in the survey itself)

---

## Survey Title

**"How was 'From Plug to Steam'?"**

Subtitle: Your honest feedback helps us create better resources. Takes less than 2 minutes.

---

## Questions

### Question 1: Lesson Viewing

**Did you get to see the full lesson?**

Type: Multiple choice (single select)

| Option | Value |
|--------|-------|
| Yes, I saw the whole thing | `viewed_full` |
| I saw parts of it | `viewed_partial` |
| I haven't viewed it yet | `not_viewed` |

---

### Question 2: Google Drive Access

**How easy was it to access the lesson on Google Drive?**

Type: Linear scale (1-5)

```
1 - Very difficult
2 - Difficult
3 - Neutral
4 - Easy
5 - Very easy
```

**Purpose:** Understand if Google Drive delivery method works well for teachers

---

### Question 3: Content Quality

**How would you rate the quality of the content?**

Type: Linear scale (1-5 stars)

```
1 ⭐ - Poor quality
2 ⭐⭐ - Below expectations
3 ⭐⭐⭐ - Met expectations
4 ⭐⭐⭐⭐ - Above expectations
5 ⭐⭐⭐⭐⭐ - Excellent quality
```

---

### Question 4: Classroom Use

**Would you use this lesson with your students?**

Type: Multiple choice (single select)

| Option | Value |
|--------|-------|
| Definitely yes | `definitely_yes` |
| Probably yes | `probably_yes` |
| I'm not sure | `not_sure` |
| Probably not | `probably_not` |

---

### Question 5: Favorite Aspects

**What did you like most about the lesson?** (Select all that apply)

Type: Checkbox (multiple select)

| Option | Insight |
|--------|---------|
| The explanation video | Values video content |
| The hands-on activities | Likes interactive learning |
| The slides/presentation | Values visual aids |
| The interactive simulation | Understands ModelIt value |
| The teacher guides | Uses support materials |
| Other: [text field] | Custom feedback |

---

### Question 6: Improvement Suggestions

**What could we improve?** (Optional)

Type: Long text (paragraph)

Placeholder: "Share any suggestions, challenges, or ideas..."

**Purpose:** Gather honest product feedback for future iterations

---

### Question 7: Grade Level

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

### Question 8: Webinar Interest

**Would you be interested in joining a free webinar where we show more lessons like this?**

Type: Multiple choice (single select)

| Option | Segmentation Action |
|--------|---------------------|
| Yes, I'm interested | → Email 4 (Eventbrite webinar invite) |
| Maybe | → Email 5 (TPT resources) |
| No, thanks | → Email 5 (TPT resources) |

---

## Hidden Fields (Auto-populated)

These fields should be pre-filled from the survey link using URL parameters:

| Field | Parameter | Example |
|-------|-----------|---------|
| Contact Email | `email` | `?email={{contact.email}}` |
| HubSpot Contact ID | `hs_id` | `?hs_id={{contact.hs_object_id}}` |
| View Date | `view_date` | `?view_date={{view_date}}` |

**Example Survey Link:**
```
https://forms.gle/XXXXX?email={{contact.email}}&hs_id={{contact.hs_object_id}}
```

---

## Segmentation Rules Based on Responses

### Webinar Invite (→ Email 4: Eventbrite)

Criteria:
- Question 8 (Webinar interest) = "Yes, I'm interested"

**Action:** Add to list "Webinar Interested", send Email 4 with Eventbrite link

### TPT Resources (→ Email 5)

Criteria (ANY of the following):
- Question 8 (Webinar interest) = "Maybe" or "No, thanks"
- Did not complete survey within 5 days

**Action:** Add to list "TPT Path", send Email 5

### Gift Card (→ Bonus Email)

Criteria:
- Survey completed (any responses)

**Action:** Send Starbucks $5 e-gift card code via email within 48 hours

---

## Important Notes

1. **NO mention of the $5 gift card in the survey itself** - The incentive is communicated in the email (Email 3) that links to the survey, not within the survey form.

2. **Focus on honest feedback** - The survey is designed to get genuine opinions, not to sell. Keep it neutral and professional.

3. **Short and respectful** - Teachers are busy. 8 questions, 2 minutes max.

---

## Integration with HubSpot

### Google Forms + Zapier

```
Google Form Submission
    ↓ (Zapier trigger)
Find HubSpot Contact by email
    ↓
Update Contact Properties:
    - survey_completed = true
    - survey_rating = [Q3 value]
    - survey_webinar_interest = [Q8 value]
    - survey_access_ease = [Q2 value]
    - survey_would_use = [Q4 value]
    ↓
Add to appropriate list based on Q8
    ↓
Trigger gift card delivery workflow
```

---

## HubSpot Properties to Update

After survey completion, update these contact properties:

| Property Name | Type | Mapped From |
|---------------|------|-------------|
| `survey_completed` | Boolean | Form submitted = true |
| `survey_date` | Date | Submission timestamp |
| `survey_viewed_lesson` | Dropdown | Question 1 |
| `survey_access_ease` | Number (1-5) | Question 2 |
| `survey_rating` | Number (1-5) | Question 3 |
| `survey_would_use` | Dropdown | Question 4 |
| `survey_liked_features` | Multi-checkbox | Question 5 |
| `survey_improvement_notes` | Text | Question 6 |
| `survey_grade_taught` | Dropdown | Question 7 |
| `survey_webinar_interest` | Dropdown | Question 8 |

---

## Thank You Page Content

After submission, show a simple thank you message:

```
Thank you for your feedback! 🎉

Your $5 Starbucks gift card will arrive in your inbox
within 48 hours.

In the meantime, explore more lessons in our TPT store:
[LINK: Visit TPT Store]
```

---

## Gift Card Delivery Process

### Steps:

1. **Weekly check:** Review new survey responses in Google Sheets
2. **Verify:** Confirm the response is legitimate (not spam)
3. **Send code:** Use the gift card email template (see email_templates_v2.md)
4. **Mark sent:** Update `gift_card_sent = true` in HubSpot
5. **Track:** Log code + email in Gift Card Spreadsheet

### Gift Card Spreadsheet Columns:

| Column | Description |
|--------|-------------|
| Code | Starbucks e-gift card code |
| Amount | $5 |
| Status | Available / Sent / Redeemed |
| Sent To | Teacher email |
| Date Sent | When the code was emailed |
| Survey Date | When they completed the survey |

### Budget:

| Item | Cost |
|------|------|
| 50 Starbucks e-gift cards x $5 | $250 |
| Sending fees | $0 (manual) |
| **Total budget** | **$250** |
| Expected redemptions (~40%) | ~$200 |

---

## Survey Analytics to Track

| Metric | Target | Calculation |
|--------|--------|-------------|
| Response rate | >40% | Responses / Survey emails sent |
| Average content rating (Q3) | >4.0 | Sum of Q3 / Total responses |
| Average access ease (Q2) | >4.0 | Sum of Q2 / Total responses |
| "Would use" rate (Q4) | >60% | "Definitely" + "Probably" / Total |
| Webinar interest (Q8) | >30% | "Yes" / Total responses |
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
- Create new spreadsheet: "From Plug to Steam - Survey Responses Jan 2026"
- Connect to Zapier for HubSpot integration

---

## Testing Checklist

Before launching the survey:

- [ ] All 8 questions display correctly
- [ ] Hidden fields populate from URL parameters
- [ ] Thank you page displays correctly
- [ ] Responses save to spreadsheet
- [ ] Zapier/integration triggers correctly
- [ ] HubSpot properties update properly
- [ ] Gift card delivery workflow triggers
- [ ] Test with your own email first
- [ ] Verify no mention of $5 in the survey form itself

---

*Last updated: January 2026*
