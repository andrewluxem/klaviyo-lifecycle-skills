# Roadmap

Order within each stage is build order. Dates are intentionally left off.

## Now

- Repo scaffold: README, license, contributing guide, changelog.
- Annotated authoring template at `skills/_template/`.
- Smoke tests at `tests/test_skills.py`.
- CI that runs the smoke tests on every push and pull request.

## Next: Wave 1

Built in this order, each shipped as its own pull request:

1. `welcome-series`
2. `abandonment-recovery`
3. `post-purchase`
4. `winback-reactivation`
5. `replenishment`
6. `sunset-suppression`
7. `pre-send-qa`

`pre-send-qa` closes out the wave because it draws on the QA sections of the six programs before it.

## Later: Wave 2 and cross-cutting

- `vip-loyalty`
- `back-in-stock-price-drop`
- `referral-advocacy`
- `lead-nurture`
- `sms-program`: compliance-first. Consent capture and records, quiet hours, and STOP and HELP handling come before any content or timing guidance.
- `seasonal-campaign-calendar`
- `brief-to-build`
- `program-scorer`

## Someday

- A docs site that renders each skill as a readable page.
- Video walkthroughs of skills applied to real builds.
- Community teardowns: contributed audits of public lifecycle programs, scored with `program-scorer`.
