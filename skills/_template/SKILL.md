---
name: _template
description: Annotated authoring template that documents what belongs in each section of a Klaviyo lifecycle skill.
---

# Skill authoring template

Copy this folder to `skills/<your-skill-name>/`, rename `name` in the frontmatter to match the folder, and replace every annotation below with real content. Delete the annotation blocks (lines starting with `>`) once a section is written.

A good skill encodes how a senior lifecycle marketer would design the program. It explains what good looks like and why. It does not teach an agent where to click in Klaviyo, and it does not restate the API.

## Frontmatter

```yaml
---
name: welcome-series          # must match the folder name exactly
description: One sentence that says what the skill does and when to load it.
---
```

> The `description` is what an agent reads when deciding whether to load the skill. Make it specific: name the program, the actions (build, audit, optimize), and the scope. One sentence.

## Ground rules every skill follows

- Skills describe programs, not API surface.
- Skills are read-only. They guide analysis, builds, audits, and QA. They never send email or SMS, and they never instruct an agent to send.
- For tool names, arguments, and API shapes, defer to `klaviyo-labs/agent-context` and the live Klaviyo API or MCP catalog. Never trust a skill over the live catalog.
- Every benchmark or example number is labeled illustrative unless it cites a verifiable source.
- Plain language. No em dashes.

---

## When to use this skill

> Write three things here.
>
> 1. Trigger phrases: the words a user is likely to type. Example: "build a welcome series", "audit our welcome flow", "why is our welcome flow underperforming".
> 2. Situations: the business context that calls for this program. Example: a new store with no onboarding flow, a list-growth push, a welcome flow that converts poorly.
> 3. What this skill is NOT for, with a pointer to the sibling skill that covers it. Example: "Not for recovering shoppers who abandoned a cart. Use `abandonment-recovery`."
>
> Sibling pointers keep agents from stretching one skill to cover another program.

## Inputs

> Split inputs into two lists.
>
> Required: what the agent must have before it can design or audit anything. Typical items: the business model (DTC, subscription, marketplace), channels in scope (email, SMS, both), the brand's offer policy (discounts allowed or not), and the current flow if this is an audit.
>
> Optional: what improves the output but has a sensible default. Typical items: past performance data, brand voice guide, catalog structure, consent and compliance constraints by region.
>
> Close the section with this instruction, adapted as needed:
>
> "If a required input is missing, ask for it. Do not guess. If an optional input is missing, state the default you are assuming and continue."

## Program blueprint

> This is the heart of the skill. Cover each subsection below.

### Objective and audience

> One or two sentences on what the program exists to do and who enters it. Name the single outcome that matters most (for example, first purchase) and the audience boundary (for example, new subscribers with no order history).

### Message architecture

> List each touch in order. For every touch give:
>
> - Purpose: why this touch exists.
> - Timing: when it sends relative to the trigger or the previous touch.
> - Channel: email, SMS, or either.
> - The job it does: what the recipient should think, feel, or do after it.
>
> Treat timing as guidance with reasoning, not a rigid rule. Write "within the first hour, because intent is highest right after signup" instead of "send at 60 minutes". The reasoning lets an agent adapt the timing to a brand that differs from the default.
>
> A table works well here. See `references/benchmarks.md` for the timing table skeleton.

### Splits and personalization

> Describe each branch the program needs and the reason for it. Common splits: purchased versus not, channel consent, first-time versus repeat buyer, product category, source of signup. For each split say what changes on each side and why that difference matters.

### Exits and suppression

> Spell out who leaves the program and when. Cover the conversion exit (for example, placed an order), overlap with other flows (for example, suppress if the profile entered abandonment recovery), and consent changes (unsubscribed, SMS STOP). Missing exits are the most common source of customer complaints, so be explicit.

### Content blocks

> Describe each content block by the job it does, not by fixed copy. Example: "Proof block: shows that people like the recipient already trust the brand, using reviews or UGC", not a scripted headline. Agents write the copy from the brand's voice. The skill defines what each block must accomplish and any fallback it needs when data is missing.

## Klaviyo build mapping

> Map the blueprint to Klaviyo objects. Cover each item and say why it is set that way.
>
> - Flow trigger: list, segment, metric, price drop, or date property, and which one.
> - Profile filters: who is allowed into the flow at all.
> - Flow filters: conditions checked before every step (for example, has not placed an order since starting this flow).
> - Conditional splits: where the flow branches and on what condition.
> - Required catalog or event data: properties the templates and splits depend on (for example, `$value`, product image URL, category). Name what breaks if the data is missing.
>
> Keep the detail at the level of program design. `references/klaviyo-build.md` holds the longer build notes.
>
> Ground rule, include it in every real skill: for tool names, arguments, and API shapes, defer to `klaviyo-labs/agent-context` and the live Klaviyo API or MCP catalog. Never trust the skill over the live catalog.

## QA

> Define what "ready to ship" means for this program as a checklist an agent can walk through. Cover links, dynamic content fallbacks, audience and filter logic, timing, consent and compliance, and rendering. `references/qa-checklist.md` holds the full list.
>
> State plainly that the skill guides QA and never sends. Test sends, previews, and go-live are human actions. The agent reports what it found and what a person should verify.

## Measurement

> Cover four things.
>
> - Primary KPI: the one number that says whether the program works (for example, placed-order rate per recipient).
> - Guardrail metrics: numbers that must not get worse while chasing the KPI (unsubscribe rate, spam complaint rate, discount cost).
> - Attribution: which attribution window and model to read, and the known bias of each.
> - Holdout guidance: when a holdout group is worth running, how to size it, and how long to run it.
>
> Label every benchmark or example number illustrative unless it cites a verifiable source. `references/measurement.md` holds the full template.

## Worked example

> Point to `examples/example-brief.md`. The example walks from a short brief to a finished build spec so an agent can see the skill applied end to end.

See `examples/example-brief.md`.

---

## Folder anatomy

```
skills/<skill-name>/
  SKILL.md                    # this file, filled in
  references/
    benchmarks.md             # timing table and labeled benchmarks
    klaviyo-build.md          # trigger, filters, splits, data
    qa-checklist.md           # ready-to-ship checklist
    measurement.md            # KPI, guardrails, attribution, holdouts
  scripts/
    validate.py               # optional deterministic checks
  examples/
    example-brief.md          # brief to build spec walkthrough
```

Keep `SKILL.md` focused on decisions and reasoning. Push long tables and checklists into `references/` so the main file stays readable. Use `scripts/` only for checks that should give the same answer every time, such as timing math or naming conventions.
