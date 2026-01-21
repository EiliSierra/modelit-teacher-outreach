# Implementation Checklist - ModelIt Teacher Outreach Campaign

## Overview

This checklist provides step-by-step tasks to implement the Teacher Outreach campaign. Follow each phase in order to ensure a successful launch.

**Estimated Total Time:** 3-4 days of setup before launch

---

## Phase 1: Content Preparation (Day 1)

### 1.1 Free Lesson Package

- [ ] **Verify lesson files exist**
  - Location: `D:\Alexandria´s Design\ModelIt\8th Grade\From Plug to Steam How Energy Boils Water\`
  - Files needed:
    - [ ] `From Plug to Steam How Energy Boils Water.zip`
    - [ ] `Teacher Guide. From Plug to Steam How Energy Boils Water.pdf`
    - [ ] `Activity Pack. From Plug to Steam How Energy Boils Water.pdf`
    - [ ] `From Plug to Steam – How Energy Boils Water.pptm`
    - [ ] `READ FIRST — Quick Start for Teachers.pdf`
    - [ ] `Teacher Lesson Walkthrough. From Plug to Steam (1).mp4`

- [ ] **Upload lesson to hosting**
  - Option A: Google Drive (shareable link)
  - Option B: Dropbox (shareable link)
  - Option C: Direct download from HubSpot file manager
  - [ ] Copy download link: `____________________________`

- [ ] **Test download link**
  - [ ] Open in incognito browser
  - [ ] Verify file downloads correctly
  - [ ] Check file size is reasonable

### 1.2 Survey Setup

- [ ] **Create Google Form**
  - [ ] Go to https://forms.google.com
  - [ ] Create new form titled: "How was 'From Plug to Steam'?"
  - [ ] Add all 7 questions from `docs/survey_questions.md`

- [ ] **Configure form settings**
  - [ ] Collect email addresses: ON
  - [ ] Limit to 1 response: ON
  - [ ] Confirmation message: Custom thank you text

- [ ] **Enable URL parameters**
  - [ ] Add `?email=` pre-fill for contact email
  - [ ] Test with: `?email=test@example.com`

- [ ] **Create responses spreadsheet**
  - [ ] Link form to Google Sheets
  - [ ] Name sheet: "From Plug to Steam - Survey Responses"

- [ ] **Copy survey link**: `____________________________`

### 1.3 Landing Page (Optional)

- [ ] **Decide: Landing page or direct download?**
  - [ ] Option A: Direct download link in email (simpler)
  - [ ] Option B: Landing page with form (better tracking)

If creating landing page:
- [ ] Create in HubSpot Landing Pages
- [ ] Add form: Name, Email, School, Grade
- [ ] Add lesson description and benefits
- [ ] Set thank you action: redirect to download
- [ ] Publish and copy URL: `____________________________`

---

## Phase 2: HubSpot Configuration (Day 2)

### 2.1 Contact Properties

Create these custom properties in HubSpot (Settings → Properties):

- [ ] `downloaded_lesson` (Single checkbox)
- [ ] `download_date` (Date picker)
- [ ] `survey_completed` (Single checkbox)
- [ ] `survey_date` (Date picker)
- [ ] `survey_rating` (Number, 1-5)
- [ ] `survey_lesson_used` (Dropdown: used_full, used_partial, plan_to_use, did_not_use)
- [ ] `survey_webinar_interest` (Dropdown: yes, maybe, no)
- [ ] `webinar_registered` (Single checkbox)
- [ ] `webinar_attended` (Single checkbox)
- [ ] `tpt_clicked` (Single checkbox)
- [ ] `purchased_tpt` (Single checkbox)
- [ ] `lead_score` (Number)

### 2.2 Contact Lists

Create these lists in HubSpot (Contacts → Lists):

- [ ] **Teachers K12 - Carlsbad**
  - Type: Static
  - Import 342 contacts from scraper data

- [ ] **Downloaded Free Lesson**
  - Type: Active
  - Criteria: `downloaded_lesson` = true

- [ ] **Survey - Hot Leads**
  - Type: Active
  - Criteria: `survey_completed` = true AND `survey_rating` >= 4

- [ ] **Survey - Cold Leads**
  - Type: Active
  - Criteria: `survey_completed` = true AND `survey_rating` < 4

- [ ] **Survey - No Response**
  - Type: Active
  - Criteria: `downloaded_lesson` = true AND `survey_completed` = false AND `download_date` < 7 days ago

- [ ] **Webinar Registered**
  - Type: Active
  - Criteria: `webinar_registered` = true

- [ ] **Webinar Attended**
  - Type: Active
  - Criteria: `webinar_attended` = true

- [ ] **TPT Visitors**
  - Type: Active
  - Criteria: `tpt_clicked` = true

### 2.3 Email Templates

Create these email templates in HubSpot (Marketing → Email):

- [ ] **Email 1: Free Lesson Offer**
  - Copy content from `docs/email_templates_v2.md`
  - Add download button with UTM parameters
  - Test personalization: `{{contact.firstname}}`

- [ ] **Email 2: Reminder**
  - Copy content from templates doc
  - Same download link

- [ ] **Email 3: Feedback Survey**
  - Copy content
  - Add survey link with email parameter

- [ ] **Email 4: Webinar Invite**
  - Copy content
  - Add webinar registration link
  - Leave `{{webinar_date}}` and `{{webinar_time}}` as placeholders

- [ ] **Email 5: More Resources**
  - Copy content
  - Add TPT store link with UTM

- [ ] **Email 6: Post-Webinar Replay**
  - Copy content
  - Add replay link, slides link
  - Add discount code: WEBINAR20

- [ ] **Email 7: Discount Reminder**
  - Copy content
  - Add TPT link with discount parameter

- [ ] **Email 8: Final Follow-up**
  - Copy content
  - Add Calendly link for demo scheduling

### 2.4 UTM Parameters

Verify all email links use proper UTM tracking:

```
?utm_source=hubspot&utm_medium=email&utm_campaign=free_lesson_jan2026&utm_content={{email_number}}
```

- [ ] Email 1: `utm_content=email1_free_lesson`
- [ ] Email 2: `utm_content=email2_reminder`
- [ ] Email 3: `utm_content=email3_survey`
- [ ] Email 4: `utm_content=email4_webinar_hot`
- [ ] Email 5: `utm_content=email5_tpt_cold`
- [ ] Email 6: `utm_content=email6_replay`
- [ ] Email 7: `utm_content=email7_discount_reminder`
- [ ] Email 8: `utm_content=email8_final_followup`

---

## Phase 3: Automation Setup (Day 3)

### 3.1 Workflows

Create these workflows in HubSpot (Automation → Workflows):

#### Workflow 1: Initial Email Sequence

- [ ] **Trigger:** Contact enrolled in list "Teachers K12 - Carlsbad"
- [ ] **Actions:**
  1. Send Email 1 (Free Lesson)
  2. Delay 3 days
  3. IF/THEN branch:
     - IF `downloaded_lesson` = false → Send Email 2 (Reminder)
     - IF `downloaded_lesson` = true → End this branch
  4. Delay 7 days (total 10 days from start)
  5. IF `downloaded_lesson` = true → Send Email 3 (Survey)
  6. End workflow

#### Workflow 2: Survey Segmentation

- [ ] **Trigger:** `survey_completed` = true
- [ ] **Actions:**
  1. IF/THEN branch based on `survey_rating`:
     - IF rating >= 4 AND `survey_webinar_interest` = "yes" or "maybe":
       - Add to list "Survey - Hot Leads"
       - Delay 1 day
       - Send Email 4 (Webinar Invite)
     - IF rating < 4 OR `survey_webinar_interest` = "no":
       - Add to list "Survey - Cold Leads"
       - Delay 1 day
       - Send Email 5 (More Resources)
  2. End workflow

#### Workflow 3: Survey Non-Responders

- [ ] **Trigger:** Contact in "Downloaded Free Lesson" list for 12 days AND `survey_completed` = false
- [ ] **Actions:**
  1. Add to list "Survey - No Response"
  2. Send Email 5 (More Resources)
  3. End workflow

#### Workflow 4: Post-Webinar Sequence

- [ ] **Trigger:** `webinar_attended` = true OR `webinar_registered` = true (run day after webinar)
- [ ] **Actions:**
  1. Send Email 6 (Replay + Discount)
  2. Delay 3 days
  3. IF `tpt_clicked` = false AND `webinar_attended` = true:
     - Send Email 7 (Discount Reminder)
  4. Delay 4 days
  5. IF `purchased_tpt` = false:
     - Send Email 8 (Final Follow-up)
  6. End workflow

#### Workflow 5: Lead Score Updates

- [ ] **Create individual workflows for each scoring action** (see `docs/lead_scoring.md`)
- [ ] Or use calculated property if HubSpot plan supports it

### 3.2 Google Forms → HubSpot Integration

Option A: Using Zapier

- [ ] Create Zapier account (if not exists)
- [ ] Create new Zap:
  - **Trigger:** New Google Forms response
  - **Action 1:** Find HubSpot contact by email
  - **Action 2:** Update HubSpot contact:
    - `survey_completed` = true
    - `survey_date` = today
    - `survey_rating` = Q2 response
    - `survey_lesson_used` = Q1 response
    - `survey_webinar_interest` = Q7 response
- [ ] Test Zap with sample submission
- [ ] Turn on Zap

Option B: Using HubSpot Forms (if preferred)

- [ ] Recreate survey as HubSpot form
- [ ] Map fields to contact properties
- [ ] Embed form or use HubSpot landing page

---

## Phase 4: Testing (Day 4)

### 4.1 Email Tests

- [ ] **Send test emails to yourself**
  - [ ] Email 1: Check links, personalization, mobile view
  - [ ] Email 2: Same checks
  - [ ] Email 3: Verify survey link works with email parameter
  - [ ] Email 4: Check webinar registration link
  - [ ] Email 5: Verify TPT links with UTM
  - [ ] Email 6: Check replay link, discount code
  - [ ] Email 7: Verify discount code display
  - [ ] Email 8: Check Calendly link

### 4.2 Workflow Tests

- [ ] **Create test contact**
  - Use your personal email
  - Add to "Teachers K12 - Carlsbad" list

- [ ] **Verify Email 1 triggers**
  - [ ] Email received?
  - [ ] Personalization correct?
  - [ ] Links work?

- [ ] **Simulate download**
  - Set `downloaded_lesson` = true manually
  - Verify workflow moves to next step

- [ ] **Submit test survey**
  - Fill out Google Form with test email
  - [ ] Verify Zapier updates HubSpot
  - [ ] Verify segmentation workflow triggers

### 4.3 Link Tests

- [ ] **Test all UTM links in Google Analytics**
  - Visit TPT link from email
  - Verify UTM parameters appear in GA

- [ ] **Test download link**
  - Click download from email
  - Verify file downloads correctly

### 4.4 Mobile Tests

- [ ] **View emails on mobile device**
  - [ ] Buttons are tappable (min 44px)
  - [ ] Text is readable (min 16px)
  - [ ] Layout is single column
  - [ ] Images load properly

---

## Phase 5: Launch Preparation

### 5.1 Final Verification

- [ ] **Contacts ready**
  - [ ] 342 contacts imported to "Teachers K12 - Carlsbad"
  - [ ] Email addresses validated (no bounces expected)
  - [ ] First names populated (for personalization)

- [ ] **All workflows active**
  - [ ] Workflow 1: Initial sequence
  - [ ] Workflow 2: Survey segmentation
  - [ ] Workflow 3: Survey non-responders
  - [ ] Workflow 4: Post-webinar (create when webinar scheduled)
  - [ ] Workflow 5: Lead scoring

- [ ] **Integrations working**
  - [ ] Google Forms → Zapier → HubSpot tested
  - [ ] UTM tracking verified

- [ ] **Backup plan**
  - [ ] Know how to pause workflows if issues arise
  - [ ] Have support contact ready

### 5.2 Schedule Launch

- [ ] **Choose launch day**
  - Recommended: Tuesday or Wednesday
  - Avoid: Monday (inbox clutter), Friday (weekend)
  - Best time: 10 AM - 12 PM recipient's timezone

- [ ] **Schedule Email 1**
  - Use HubSpot scheduling feature
  - Set for optimal send time
  - Launch date: `____________________________`

---

## Phase 6: Post-Launch Monitoring

### Day 1 (Launch Day)

- [ ] **Monitor email delivery**
  - Check HubSpot email dashboard
  - Look for: Delivered %, Open %, Bounce %
  - Target: >95% delivered, >20% opens

- [ ] **Check for issues**
  - Any reply complaints?
  - Unsubscribe spike?
  - Bounce rate normal?

### Day 3 (Email 2)

- [ ] **Email 2 sending to non-downloaders**
  - Verify workflow triggered correctly
  - Check delivery metrics

- [ ] **Review download stats**
  - How many downloaded? Target: >30%
  - Update `downloaded_lesson` property accurate?

### Day 10 (Survey Email)

- [ ] **Email 3 sent to downloaders**
  - Verify correct audience received
  - Check survey link working

- [ ] **Monitor survey responses**
  - Check Google Sheets
  - Verify Zapier updating HubSpot

### Day 12+ (Segmentation)

- [ ] **Verify segmentation working**
  - Hot leads receiving Email 4?
  - Cold leads receiving Email 5?

- [ ] **Review lead scores**
  - Scores calculating correctly?
  - Segment distribution reasonable?

### Ongoing

- [ ] **Weekly metrics review**
  - Open rates by email
  - Click rates
  - Downloads
  - Survey responses
  - Lead score distribution

- [ ] **Optimize as needed**
  - A/B test subject lines
  - Adjust send times
  - Refine segmentation

---

## Quick Reference: Key Links

| Item | Link |
|------|------|
| Lesson Download | `____________________________` |
| Survey Form | `____________________________` |
| Survey Responses | `____________________________` |
| TPT Store | https://www.teacherspayteachers.com/store/modelit |
| HubSpot Portal | `____________________________` |
| Zapier Dashboard | https://zapier.com/app/dashboard |
| Webinar Registration | `____________________________` |
| Calendly Demo | `____________________________` |

---

## Quick Reference: Property Values

| Property | Possible Values |
|----------|-----------------|
| `survey_lesson_used` | used_full, used_partial, plan_to_use, did_not_use |
| `survey_webinar_interest` | yes, maybe, no |
| `lead_score` | 0-200+ (calculated) |

---

## Troubleshooting

### Email not sending

1. Check workflow is active
2. Verify contact meets enrollment criteria
3. Check contact not in suppression list
4. Review workflow history for errors

### Survey not updating HubSpot

1. Check Zapier is turned on
2. Verify email in form matches HubSpot contact
3. Check Zapier task history for errors
4. Test with new submission

### Lead score not calculating

1. Verify scoring workflows are active
2. Check property updates triggering correctly
3. Review workflow enrollment logs

---

## Success Criteria

### Week 1

- [ ] Email 1 open rate > 25%
- [ ] Download rate > 20%
- [ ] No major technical issues

### Week 2

- [ ] Survey response rate > 30%
- [ ] Average rating > 3.5 stars
- [ ] Hot leads identified

### Month 1

- [ ] Download rate > 30%
- [ ] Survey response > 40%
- [ ] TPT visits > 25%
- [ ] At least 1 purchase

---

*Checklist Version: 1.0 | January 2026*
