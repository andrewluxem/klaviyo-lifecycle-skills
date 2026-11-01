# klaviyo-lifecycle-skills

Planned agent skills for designing, auditing, and QA-ing Klaviyo lifecycle programs, in the SKILL.md format that Claude Code, Codex, Cursor, GitHub Copilot, and Gemini CLI read.

**Status: early.** The repo has an annotated authoring template and nine stub skill folders. No skill has program content yet; each stub holds its frontmatter and TODO markers.

## The idea

Most Klaviyo skills teach an agent how to click around Klaviyo. These are meant to teach it what good looks like. Each skill is planned as one retention or lifecycle program, designed the way a senior lifecycle marketer would: the strategy, the flow architecture, timing and splits, content blocks, pre-send QA, and measurement. The agent brings the tool access. The skill brings the judgment.

## Install

```bash
git clone https://github.com/andrewluxem/klaviyo-lifecycle-skills.git
cd klaviyo-lifecycle-skills
cp -r skills/<skill> ~/.claude/skills/
```

Replace `<skill>` with a folder name from the catalog below, for example `skills/welcome-series`. For other agents, copy the skill folder into the location your agent reads skills from. Today every folder is a stub, so an installed skill gives the agent section headings and TODO markers, not a program.

## Skills catalog

Fifteen skills are planned. Nine have a stub folder in `skills/` today; the six Wave 2 skills have no folder yet. None has program content. See [ROADMAP.md](ROADMAP.md) for build order.

### Wave 1: core programs

| Skill | What it covers | Status |
|---|---|---|
| `welcome-series` | Subscriber-to-first-purchase onboarding: message architecture, timing, splits, QA, measurement | Stub |
| `abandonment-recovery` | Browse, cart, and checkout recovery across email and SMS | Stub |
| `post-purchase` | Thank you, cross-sell, review capture, replenishment handoff | Stub |
| `winback-reactivation` | Lapsed buyer and customer recovery: segmentation, offer strategy, timing | Stub |
| `replenishment` | Consumable reorder timing: reorder modeling, timing, splits | Stub |
| `sunset-suppression` | List hygiene: sunset flow design, suppression rules, deliverability guardrails | Stub |

### Wave 2: expansion programs

| Skill | What it covers | Status |
|---|---|---|
| `vip-loyalty` | Recognition and retention for high-value customers | Planned, no folder yet |
| `back-in-stock-price-drop` | Demand capture when inventory returns or prices fall | Planned, no folder yet |
| `referral-advocacy` | Turning satisfied customers into referrers and reviewers | Planned, no folder yet |
| `lead-nurture` | Moving non-buyers toward a first purchase over a longer cycle | Planned, no folder yet |
| `sms-program` | A compliance-first SMS program: consent, quiet hours, STOP handling | Planned, no folder yet |
| `seasonal-campaign-calendar` | Planning campaigns around the retail calendar without burning the list | Planned, no folder yet |

### Cross-cutting

| Skill | What it covers | Status |
|---|---|---|
| `pre-send-qa` | Pre-send QA for any email or SMS program: broken links, missing fallbacks, audience errors, compliance gaps | Stub |
| `brief-to-build` | Turns a creative or campaign brief into a shippable Klaviyo build spec | Stub |
| `program-scorer` | Scores any Klaviyo flow against a rubric and returns prioritized fixes | Stub |

## Skill anatomy

Each skill will follow this layout once it is written:

```
skills/<skill-name>/
  SKILL.md                    # frontmatter + the program, section by section
    ## When to use this skill   triggers, situations, and what it is not for
    ## Inputs                   required vs optional; ask, do not guess
    ## Program blueprint        objective, touches, timing, splits, exits, content blocks
    ## Klaviyo build mapping    trigger, filters, splits, required data
    ## QA                       what ready to ship means
    ## Measurement              KPI, guardrails, attribution, holdouts
    ## Worked example           pointer to examples/
  references/                 benchmarks, build notes, QA checklist, measurement template
  scripts/                    optional deterministic checks
  examples/                   brief-to-build-spec walkthroughs
```

`skills/_template/` is the fully annotated authoring template. Start there.

## Ground rules

- Skills describe programs, not API surface. They encode design judgment, not endpoint documentation.
- For tool names, arguments, and API shapes, defer to [klaviyo-labs/agent-context](https://github.com/klaviyo-labs/agent-context) and the live Klaviyo API or MCP catalog. When a skill and the live catalog disagree, the catalog wins.
- Skills are read-only by design. They guide analysis, builds, audits, and QA. They never send email or SMS.
- Benchmark and example numbers are labeled illustrative unless they cite a verifiable source.
- Every skill folder must pass the smoke tests: `python tests/test_skills.py`. CI runs them on every push and pull request.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request, and check [ROADMAP.md](ROADMAP.md) to see what is planned.

## License

MIT. See [LICENSE](LICENSE).
