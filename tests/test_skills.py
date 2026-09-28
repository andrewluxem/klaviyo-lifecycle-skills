#!/usr/bin/env python3
"""Smoke tests for every skill folder under skills/.

Checks, per folder:
  - SKILL.md exists and opens with YAML frontmatter.
  - Frontmatter has a non-empty `name` and `description`.
  - `name` matches the folder name (except for `_template`).
  - Non-template skills contain every required section heading.
  - `references/` and `examples/` directories exist.

Standard library only, so it runs anywhere Python 3 runs with no install step.
Prints `OK: N skill folders validated` and exits 0 on success.
Prints each failure and exits 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
TEMPLATE = "_template"

REQUIRED_SECTIONS = [
    "## When to use this skill",
    "## Inputs",
    "## Program blueprint",
    "## Klaviyo build mapping",
    "## QA",
    "## Measurement",
]

REQUIRED_DIRS = ["references", "examples"]


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Return top-level `key: value` pairs from a leading `---` block, or None if absent.

    Deliberately minimal: skill frontmatter is flat scalars, so a full YAML parser
    is not needed and would add a dependency.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            value = match.group(2).strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            fields[match.group(1)] = value
    return None  # opening fence with no closing fence


def has_heading(text: str, heading: str) -> bool:
    return re.search(rf"^{re.escape(heading)}\s*$", text, re.MULTILINE) is not None


def validate(folder: Path) -> list[str]:
    errors: list[str] = []
    label = folder.name
    skill_md = folder / "SKILL.md"

    if not skill_md.is_file():
        errors.append(f"{label}: missing SKILL.md")
    else:
        text = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{label}: SKILL.md has no valid YAML frontmatter block")
        else:
            name = fm.get("name", "")
            if not name:
                errors.append(f"{label}: frontmatter missing `name`")
            elif label != TEMPLATE and name != label:
                errors.append(f"{label}: frontmatter name `{name}` does not match folder name")
            if not fm.get("description", ""):
                errors.append(f"{label}: frontmatter missing `description`")

        if label != TEMPLATE:
            for heading in REQUIRED_SECTIONS:
                if not has_heading(text, heading):
                    errors.append(f"{label}: SKILL.md missing section `{heading}`")

    for dirname in REQUIRED_DIRS:
        if not (folder / dirname).is_dir():
            errors.append(f"{label}: missing `{dirname}/` directory")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"FAIL: skills directory not found at {SKILLS_DIR}")
        return 1

    folders = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not folders:
        print("FAIL: no skill folders found under skills/")
        return 1

    failures: list[str] = []
    for folder in folders:
        failures.extend(validate(folder))

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"{len(failures)} failure(s) across {len(folders)} skill folders")
        return 1

    print(f"OK: {len(folders)} skill folders validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
