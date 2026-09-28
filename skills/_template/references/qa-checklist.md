# QA checklist

> Annotated template. Adapt the items to the program. Each item should be something an agent can check and report on.
>
> This checklist guides QA. It never sends. Test sends, previews to real inboxes, and turning a flow live are human actions. The agent reports findings and names what a person should verify.

## Audience and logic

- [ ] Trigger matches the blueprint.
- [ ] Profile filters exclude everyone who should not enter.
- [ ] Flow filters stop the flow when the goal is reached (for example, a purchase).
- [ ] Splits route each audience to the intended branch.
- [ ] Overlap with other flows is handled (no profile gets two competing messages at once).

## Content

- [ ] Every link resolves and carries the expected UTM or tracking parameters.
- [ ] Every dynamic variable has a fallback for missing data.
- [ ] Discount codes, if any, are valid for the window the message implies.
- [ ] Subject line and preview text fit their purpose and are not truncated badly.

## Timing

- [ ] Delays match the timing table in `benchmarks.md`.
- [ ] Smart Send Time and quiet hours settings are intentional.

## Compliance and consent

- [ ] Email includes a working unsubscribe and a physical address.
- [ ] SMS goes only to profiles with SMS consent, respects quiet hours, and honors STOP.
- [ ] Regional rules that apply to the audience are noted for human review.

## Rendering

- [ ] Layout holds on mobile and desktop.
- [ ] Images have alt text; the message still makes sense with images off.

## Sign-off

- [ ] Findings summarized with severity (blocker, fix before launch, nice to have).
- [ ] Items that need a human check are listed separately.
