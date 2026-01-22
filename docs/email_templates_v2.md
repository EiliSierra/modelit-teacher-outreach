# Email Templates v2 - Teacher Outreach ModelIt

## Overview

This document contains the 8 email templates for the improved Teacher Outreach campaign. The new funnel focuses on **giving value first** with a free lesson before asking for commitment.

**Lesson Offered:** "From Plug to Steam: How Energy Boils Water"
**Target Audience:** 342 teachers from Carlsbad USD
**Lesson Link:** https://drive.google.com/file/d/1x5cygfmfAQdpsGzCi-ksZ3cX-kdJ7bHc/view
**Webinar:** https://www.eventbrite.com/o/modelit-k12-education-120756581127
**Goal:** Build trust → Collect feedback ($5 gift card) → Webinar (Eventbrite) → Convert to TPT sales

---

## Email Sequence Overview

```
[Email 1] Free Lesson Offer
    ↓
[Email 2] Reminder (non-downloaders only, Day 3)
    ↓
[Email 3] Feedback Survey (Day 10)
    ↓
    ├── [Email 4] Webinar Invite (hot leads: 4-5 stars)
    └── [Email 5] More Resources (cold/no response)
    ↓
[Email 6] Post-Webinar Replay + Discount (Day 14)
    ↓
[Email 7] Discount Reminder (Day 17)
    ↓
[Email 8] Final Follow-up (Day 21)
```

---

## EMAIL 1: Free Lesson Offer (Day 1)

### Subject Lines (A/B Test)
- **A:** "Free lesson: Your students will simulate boiling water"
- **B:** "A gift for your science class — view it free"

### Body

```
Hi {{contact.firstname}},

Have you ever wished your students could SEE how energy flows
through a system — not just read about it?

We created a free lesson called "From Plug to Steam: How Energy
Boils Water" that lets students build and test a digital model
of energy transfer.

In about 45 minutes, your students will:
✓ Identify components of an energy system
✓ Connect cause-and-effect relationships
✓ Run simulations to test "what if" scenarios
✓ See real-time graphs of energy flow

The lesson is NGSS-aligned (PS3.A, PS3.B) and works perfectly
for 8th grade physical science.

[BUTTON: View Free Lesson]
https://drive.google.com/file/d/1x5cygfmfAQdpsGzCi-ksZ3cX-kdJ7bHc/view

What's included:
• Teacher Guide with step-by-step instructions
• Student Activity Pack (printable + digital)
• PowerPoint slides
• Video walkthrough for you
• Direct link to the simulation — no student accounts needed

View it anytime — it's on Google Drive, no download required.
Try it with your class and let us know what you think!

Best,
The ModelIt Team

P.S. Over 150 teachers in your area have already downloaded this lesson.
```

### HubSpot Properties
- **CTA Link:** `https://drive.google.com/file/d/1x5cygfmfAQdpsGzCi-ksZ3cX-kdJ7bHc/view` with UTM: `?utm_source=hubspot&utm_medium=email&utm_campaign=free_lesson_jan2026&utm_content=email1`
- **Send to:** All contacts in "Teachers K12 - Carlsbad" list
- **Track:** Email opens, clicks on Google Drive link

---

## EMAIL 2: Reminder (Day 3)

### Trigger
Send only to contacts who:
- Received Email 1
- Did NOT click the Google Drive link

### Subject Line
"Your free energy lesson is waiting"

### Body

```
Hi {{contact.firstname}},

A few days ago we sent you a free lesson on energy transfer.

Just wanted to make sure you saw it — it's one of our most
popular resources for 8th grade science.

"From Plug to Steam" takes about 45 minutes and includes
everything you need: teacher guide, student activities,
PowerPoint, and a simulation your students can run right
in their browser.

[BUTTON: View Free Lesson]
https://drive.google.com/file/d/1x5cygfmfAQdpsGzCi-ksZ3cX-kdJ7bHc/view

No strings attached. Just a great lesson we think you'll love.

— The ModelIt Team
```

### HubSpot Properties
- **CTA Link:** Same Google Drive link with `&utm_content=email2_reminder`
- **Workflow condition:** `email_1_clicked = false`

---

## EMAIL 3: Feedback Survey + $5 Gift Card (Day 8-10)

### Trigger
Send to contacts who:
- Viewed the lesson (clicked Google Drive link)
- 5-7+ days since viewing

### Subject Line
"Quick question about the lesson (+ a $5 thank you)"

### Body

```
Hi {{contact.firstname}},

Last week you checked out "From Plug to Steam: How Energy Boils Water."

We'd love to hear what you thought!

As a thank you for your feedback, you'll receive a $5 Starbucks
gift card after completing this 2-minute survey.

[BUTTON: Take 2-Minute Survey → Get $5]
{{survey_link}}

Your honest feedback helps us create better resources for
teachers like you. Whether you loved it or have suggestions,
we want to hear it all.

Thanks for being part of the ModelIt community!

— The ModelIt Team

P.S. The $5 Starbucks gift card will be sent to your email
within 48 hours of completing the survey. ☕
```

### HubSpot Properties
- **Survey Link:** Google Form with UTM tracking
- **Workflow condition:** `viewed_lesson = true` AND `days_since_view >= 5`
- **Gift Card:** Send Starbucks $5 e-gift card code after survey completion

---

## EMAIL 4: Webinar Invitation (Day 12)

### Trigger
Send to contacts who:
- Completed the survey
- Selected "Sí, me interesa" for webinar interest

### Subject Line
"You're invited: Exclusive webinar for science teachers"

### Body

```
Hi {{contact.firstname}},

Thank you for trying "From Plug to Steam" — we're thrilled
you found it valuable!

Based on your feedback, we'd like to invite you to something special:

**Free Live Webinar: "Teaching Systems Thinking with ModelIt"**
📅 {{webinar_date}}
🕓 {{webinar_time}} PST
⏱️ 45 min + Q&A

In this webinar, you'll:
• See 3 more simulation-based lessons in action
• Learn how to integrate ModelIt into your curriculum
• Get teaching tips from experienced educators
• Ask questions live

Plus, all attendees get a special discount on our TPT store.

[BUTTON: Save My Spot on Eventbrite]
https://www.eventbrite.com/o/modelit-k12-education-120756581127

Space is limited to keep the session interactive.

See you there!

— The ModelIt Team
```

### HubSpot Properties
- **Workflow condition:** `survey_completed = true` AND `webinar_interest = "yes"`
- **Webinar Link:** https://www.eventbrite.com/o/modelit-k12-education-120756581127
- **Dynamic fields:** `{{webinar_date}}`, `{{webinar_time}}`
- **Track:** Eventbrite registration clicks

---

## EMAIL 5: More Resources (Cold/Neutral Leads)

### Trigger
Send to contacts who:
- Did not respond to survey, OR
- Gave 1-3 star rating, OR
- Selected "No thanks" for webinar interest

### Subject Line
"More lessons like the one you downloaded"

### Body

```
Hi {{contact.firstname}},

A couple weeks ago you downloaded our free lesson on energy transfer.

Whether you've used it or it's still in your "to-try" folder,
we wanted to let you know: we have more where that came from.

**Our TPT Store has 10+ simulation-based lessons including:**
• From Sun to Lunch (energy flow in living systems)
• Ecosystem Balance (predator-prey dynamics)
• Chemical Reactions in Action
• And more coming soon

All lessons include teacher guides, student activities,
and ready-to-use simulations.

[BUTTON: Browse Our TPT Store]
{{tpt_store_link}}

Or, if you prefer to see the lessons in action first,
join our upcoming free webinar:

[LINK: Register for Webinar on Eventbrite]
https://www.eventbrite.com/o/modelit-k12-education-120756581127

Happy teaching!

— The ModelIt Team
```

### HubSpot Properties
- **TPT Link:** `https://www.teacherspayteachers.com/store/modelit?utm_source=hubspot&utm_medium=email&utm_campaign=free_lesson_jan2026&utm_content=email5_tpt`
- **Workflow condition:** `survey_completed = false` OR `survey_rating < 4`

---

## EMAIL 6: Post-Webinar - Replay + Resources (Day 14)

### Trigger
Send to all contacts who:
- Registered for the webinar (regardless of attendance)

### Subject Line
"Your webinar replay + resources"

### Body

```
Hi {{contact.firstname}},

Thank you for joining our webinar!

Here's everything you need:

📹 **Webinar Replay:** {{replay_link}}
📄 **Slides (PDF):** {{slides_link}}
🎁 **Your Exclusive Discount:** Use code WEBINAR20 for 20% off
   any lesson in our TPT store (expires in 7 days)

[BUTTON: Shop TPT Store with Discount]
{{tpt_store_link}}?discount=WEBINAR20

Missed the live session? No worries — the replay covers everything.

Questions? Just reply to this email.

— The ModelIt Team
```

### HubSpot Properties
- **Discount code:** WEBINAR20 (20% off, 7-day expiration)
- **Workflow condition:** `webinar_registered = true`
- **Track:** Replay views, TPT clicks

---

## EMAIL 7: Discount Reminder (Day 17)

### Trigger
Send to contacts who:
- Received Email 6
- Did NOT click TPT link
- Attended the webinar

### Subject Line
"Your discount expires in 3 days"

### Body

```
Hi {{contact.firstname}},

Just a quick reminder: your webinar discount (20% off)
expires in 3 days.

**Our most popular lessons:**

1. "From Sun to Lunch" — Energy flow in ecosystems ($7.99 → $6.39)
2. "Ecosystem Balance" — Predator-prey dynamics ($7.99 → $6.39)
3. "Chemical Reactions" — Interactive chemistry ($8.99 → $7.19)

[BUTTON: Use My Discount Before It Expires]
{{tpt_store_link}}?discount=WEBINAR20

Your code: WEBINAR20

— The ModelIt Team
```

### HubSpot Properties
- **Workflow condition:** `webinar_attended = true` AND `tpt_clicked = false`

---

## EMAIL 8: Final Follow-up (Day 21)

### Trigger
Send to all contacts who:
- Engaged with the campaign (downloaded lesson OR registered webinar)
- Did NOT purchase on TPT

### Subject Line
"Any questions about ModelIt?"

### Body

```
Hi {{contact.firstname}},

This is our last email for now.

If you have questions about:
• How to use ModelIt in your classroom
• Which lessons fit your curriculum
• Technical setup or student access

Just reply to this email — we're happy to help.

Or, if you'd like a quick 15-minute demo call,
we can show you the platform one-on-one:

[BUTTON: Schedule a Demo]
{{calendly_link}}

Thanks for being part of the ModelIt community!

— The ModelIt Team

P.S. You can always find our lessons at:
https://www.teacherspayteachers.com/store/modelit
```

### HubSpot Properties
- **Calendly Link:** Personal demo scheduling
- **Workflow condition:** `purchased_tpt = false`

---

## BONUS EMAIL: Gift Card Delivery (After Survey Completion)

### Trigger
Send to contacts who:
- Completed the feedback survey
- `gift_card_sent = false`

### Subject Line
"Your $5 Starbucks Gift Card! ☕"

### Body

```
Hi {{contact.firstname}},

Thank you for sharing your feedback about our "From Plug to Steam"
lesson!

As promised, here's your $5 Starbucks Gift Card:

🎁 Code: {{gift_card_code}}

To redeem: Visit starbucks.com/card or the Starbucks app
and add this code.

We hope you enjoy your coffee!

— The ModelIt Team
```

### Process Notes
- **Source:** Pre-purchased Starbucks e-gift cards ($5 each)
- **Delivery:** Manual or semi-automated (check surveys weekly)
- **Tracking:** Mark `gift_card_sent = true` after sending
- **Budget:** ~$250 for 50 cards (expect ~40 redemptions)

---

## UTM Parameters Reference

| Email | UTM Content Value |
|-------|-------------------|
| Email 1 | `email1_free_lesson` |
| Email 2 | `email2_reminder` |
| Email 3 | `email3_survey` |
| Email 4 | `email4_webinar_hot` |
| Email 5 | `email5_tpt_cold` |
| Email 6 | `email6_replay` |
| Email 7 | `email7_discount_reminder` |
| Email 8 | `email8_final_followup` |

**Base UTM:**
```
?utm_source=hubspot&utm_medium=email&utm_campaign=free_lesson_jan2026&utm_content={{email_content}}
```

---

## HubSpot Contact Properties Required

| Property | Type | Purpose |
|----------|------|---------|
| `viewed_lesson` | Boolean | Clicked Google Drive link |
| `view_date` | Date | When they viewed the lesson |
| `gift_card_sent` | Boolean | Starbucks $5 code sent |
| `survey_completed` | Boolean | Filled out feedback form |
| `survey_rating` | Number (1-5) | Star rating from survey |
| `webinar_interest` | Dropdown | yes/maybe/no |
| `webinar_registered` | Boolean | Signed up for webinar |
| `webinar_attended` | Boolean | Actually attended |
| `tpt_clicked` | Boolean | Clicked any TPT link |
| `purchased_tpt` | Boolean | Confirmed purchase |
| `lead_score` | Number | Calculated automatically |

---

## Email Design Notes

### Brand Guidelines
- **Primary Color:** #2563EB (ModelIt blue)
- **Font:** System fonts (Arial, Helvetica)
- **Logo:** Include ModelIt logo in header
- **Footer:** Include unsubscribe link, physical address (CAN-SPAM)

### Mobile Optimization
- Single column layout
- Buttons minimum 44px height
- Font size minimum 16px
- Clear CTA buttons (not text links)

### Personalization
- Always use `{{contact.firstname}}` in greeting
- Fall back to "Hi there" if first name is missing:
  `{{contact.firstname | default: "there"}}`

---

## Testing Checklist

Before launching each email:

- [ ] Subject line renders correctly
- [ ] Personalization tokens work
- [ ] All links have UTM parameters
- [ ] Links open correct destinations
- [ ] Unsubscribe link works
- [ ] Mobile preview looks good
- [ ] Spam score is low (<5)
- [ ] Send test to yourself

---

## Files Location

**Lesson shared via Google Drive:**
https://drive.google.com/file/d/1x5cygfmfAQdpsGzCi-ksZ3cX-kdJ7bHc/view

**Original source files:**
`D:\Alexandria´s Design\ModelIt\8th Grade\From Plug to Steam How Energy Boils Water\`

- `From Plug to Steam How Energy Boils Water.zip` — Complete package
- `Teacher Guide. From Plug to Steam How Energy Boils Water.pdf`
- `Activity Pack. From Plug to Steam How Energy Boils Water.pdf`
- `From Plug to Steam – How Energy Boils Water.pptm`
- `READ FIRST — Quick Start for Teachers.pdf`
- `Teacher Lesson Walkthrough. From Plug to Steam (1).mp4`
