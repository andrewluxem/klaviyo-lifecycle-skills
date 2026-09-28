#!/usr/bin/env python3
"""Example deterministic check for a skill's scripts/ folder.

Pattern: a skill ships small scripts for checks that must give the same answer
every time, so the agent does not have to reason them out. This example checks a
flow's timing plan against simple rules. It reads a JSON file, never calls an
API, and never sends anything.

Usage:
    python validate.py plan.json

plan.json shape:
    {"touches": [{"name": "Welcome 1", "channel": "email", "delay_hours": 0},
                 {"name": "Welcome 2", "channel": "sms", "delay_hours": 24}]}

delay_hours is measured from the previous touch (the first touch from the trigger).
The thresholds below are illustrative defaults. Each real skill sets its own and
explains why in SKILL.md.
"""

from __future__ import annotations

import json
import sys

VALID_CHANNELS = {"email", "sms"}
MIN_GAP_HOURS = 4  # illustrative: avoid back-to-back touches
MAX_TOTAL_DAYS = 30  # illustrative: flag programs that drift too long


def check(plan: dict) -> list[str]:
    problems: list[str] = []
    touches = plan.get("touches", [])
    if not touches:
        return ["plan has no touches"]

    total_hours = 0.0
    for i, touch in enumerate(touches):
        label = touch.get("name") or f"touch {i + 1}"
        channel = touch.get("channel")
        delay = touch.get("delay_hours")

        if channel not in VALID_CHANNELS:
            problems.append(f"{label}: channel must be one of {sorted(VALID_CHANNELS)}")
        if not isinstance(delay, (int, float)) or delay < 0:
            problems.append(f"{label}: delay_hours must be a number >= 0")
            continue
        if i > 0 and delay < MIN_GAP_HOURS:
            problems.append(f"{label}: only {delay}h after the previous touch (minimum {MIN_GAP_HOURS}h)")
        total_hours += delay

    if total_hours > MAX_TOTAL_DAYS * 24:
        problems.append(f"program spans {total_hours / 24:.1f} days (review anything over {MAX_TOTAL_DAYS})")
    return problems


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as f:
        plan = json.load(f)
    problems = check(plan)
    for p in problems:
        print(f"WARN: {p}")
    if not problems:
        print("OK: timing plan passes all checks")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
