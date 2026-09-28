# Contributing

Thanks for helping build this library. The bar is simple: a skill should make an agent design the program the way a senior lifecycle marketer would.

## Propose first

Open an issue before writing a new skill. Describe the program, who it serves, and why it is distinct from the skills already in the catalog. This saves you from building something that overlaps an existing or planned skill. Fixes and improvements to existing skills can go straight to a pull request.

## Authoring steps

1. Copy the template: `cp -r skills/_template skills/<your-skill-name>`.
2. Set `name` in the frontmatter to match the folder name exactly. Write a one-sentence `description`.
3. Fill in every required section of `SKILL.md`, following the annotations in the template. Delete the annotation blocks when you are done.
4. Fill in the four files under `references/`, or remove any that do not apply and update the pointers.
5. Add a worked example under `examples/`.
6. Add scripts under `scripts/` only for checks that should give the same answer every time.
7. Run the smoke tests (below) and fix any failures.

## House style

- Plain language. Short sentences.
- No em dashes anywhere in prose. Use a colon, a comma, or a new sentence.
- Say "skill-driven workflows". Do not describe this library as "API-driven".
- Do not quote GitHub star counts in any public-facing copy.
- Label every benchmark or example number illustrative unless it cites a verifiable source.
- Skills are read-only by design. They guide analysis, builds, audits, and QA. They never send email or SMS, and they never instruct an agent to send.
- For tool names, arguments, and API shapes, defer to `klaviyo-labs/agent-context` and the live Klaviyo API or MCP catalog. Do not copy API payloads into a skill.

## Run the tests locally

```bash
python tests/test_skills.py
```

The script uses only the Python standard library. It must print `OK: N skill folders validated` before you open a pull request. CI runs the same check on every push and pull request.

## Pull requests

- One skill per pull request. Small fixes across several skills are fine in one PR if they are the same kind of fix.
- Add a line to `CHANGELOG.md` under an Unreleased heading.
- In the PR description, note any number you cite and its source.
