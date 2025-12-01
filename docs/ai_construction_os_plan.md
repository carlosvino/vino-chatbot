# AI Construction OS: Tiered Commercialization Plan

This document captures the 3-tier rollout strategy for the AI-powered Construction OS, focusing on staged validation, monetization, and data flywheel creation.

## Tier 1 – Internal Automation ("Vino-Only Efficiency")
- **Objective:** Deploy private automation stack to reduce PM cycle time by 30–50% and tighten accountability across intake → permits → billing.
- **Key Modules (MVP order):**
  1. Blueprint & code-compliance scanner (YOLOv5 + rules engine) with CRC/Title 24/ADA checks, sheet index validation, missing detail detection.
  2. Estimate builder: scope mapping to JobTread cost codes with auto line items.
  3. Intake & lead router (GoHighLevel) with zero-leak capture, voice-to-lead, duplicate detection.
  4. Daily log & change-order bot: voice memo → structured log → CO draft w/ attachments.
  5. Permit packet builder: form autofill, PDF compilation, checklists, cover sheets.
- **90-day KPIs:**
  - 100% leads contacted <15 minutes.
  - Estimating drafts <48 hrs (design) / <5 days (build).
  - <3 plan corrections per set.
  - Change orders issued <24 hrs from field note.
  - ≥20 PM hours saved per week (tracked in JobTread tasks).

## Tier 2 – Service Model ("Blueprint/Compliance Engine for Architects")
- **Concept:** Operate the internal engine as a done-for-you plan check + permit pack service for architects/GCs before launching SaaS.
- **Offer Stack & Pricing:**
  - Plan Check Lite ($349–$699): redlines, code hit-list, missing sheets.
  - Permit Ready Pack ($1,250–$2,500): forms, checklists, energy/MEP requirements, submittal index.
  - Estimate-Ready Scope ($750–$1,500): CSI mapping, quantities, assumptions.
  - Add-ons: Rush (×1.5), County (+$200), Meeting (+$250).
- **30-day GTM:** outreach to 20 architects/expediters, 5 warm intros, single-page landing with Calendly, portfolio (5 redline samples + 2 case studies), guarantee: "If your jurisdiction issues corrections on any item we flagged, we revise free."
- **Service KPIs:** 10 paying customers in 60 days, NPS ≥50, repeat rate ≥40%, ≥70% gross margin (leveraging VAs + automations).

## Tier 3 – SaaS Platform ("Subscription Marketplace")
- **Offering:** Self-serve web app + API for instant plan checks, scope seeds, permit packets, plus marketplace for regional add-ons (Title 24, soils, expediters, drafters).
- **Pricing:**
  - Starter $99/mo (5 plan checks, basic rules, PDF report).
  - Pro $299–$499/mo (unlimited checks, cost-code exports, team seats, webhooks).
  - Enterprise (custom) w/ multi-jurisdiction rulesets, SSO, SLAs, audit logs.
- **Feature Sequence:**
  1. Upload → instant rule checks (sheet coverage, egress, stairs, smoke/CO, clearances).
  2. Scope/estimate export (CSV → JobTread).
  3. Permit pack builder (city/county autofill).
  4. Marketplace for local add-ons.
  5. Public API.
- **SaaS KPIs:** Time-to-value <5 minutes, WAU/MAU ≥35%, churn <4%/mo, marketplace attach rate ≥25%.

## 12-Week Execution Timeline
1. **Weeks 1–2:** Build Tier 1 MVP (rules v0, JobTread mapper, daily log bot) + baseline KPIs/dashboards.
2. **Weeks 3–4:** Run across 3 jobs, measure time saved, refine prompts/rules, templatize COs & permit packs.
3. **Weeks 5–6:** Launch Tier 2 (landing page, case studies, outreach to 20 architects, sell 5 pilots). Deliver via VA + engine and capture testimonials.
4. **Weeks 7–9:** Harden engine with jurisdiction profiles (Napa/Sonoma/Solano), one-click reports, CSV exports.
5. **Weeks 10–12:** SaaS alpha (thin web app: upload → checks → report → CSV, Stripe + Pro waitlist). Pilot with 5 service clients and iterate weekly.

## Org & Accountability
- **CEO/GTMP:** Sales, partnerships, pricing, weekly KPI reviews.
- **PM/VA:** Intake, QA reports, CO drafts, client comms.
- **Automation Dev:** Rules engine, CSV mappers, webhooks, lightweight UI.
- **Compliance SME:** Codifies local rules, reviews edge cases.

## Outstanding Inputs Needed
1. **Top Jurisdictions & Corrections:** Provide the three most common jurisdictions (city/county) served plus their frequent correction themes.
2. **Redacted Plan Set:** Supply a sample PDF plan set for wiring v0 checks.
3. **Tier 2 Price Points:** Confirm approved price ranges (or specify adjustments).
4. **KPI Dashboard Preference:** Choose JobTread, SmartSuite, or Google Sheet for the first KPI tracker.

Once the above data is available, we can finalize rule CSV starter files, draft the services landing page, build outreach scripts, and map the pilot workflow across JobTread + GoHighLevel.
