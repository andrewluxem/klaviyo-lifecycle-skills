---
name: welcome-series
description: Build, audit, or optimize a Klaviyo welcome series that takes a new subscriber to a first purchase, covering message architecture, timing, splits, QA, and measurement.
---

# Welcome Series

> Status: Planned. This is a stub. Section bodies are TODO markers. See `skills/_template/SKILL.md` for what belongs in each section.

Scope: Subscriber-to-first-purchase onboarding.

This skill is read-only. It guides analysis, builds, audits, and QA. It never sends email or SMS.

## When to use this skill

TODO: Trigger phrases and situations that should load this skill. List what it is NOT for and point to the sibling skill that covers that case.

## Inputs

TODO: Required inputs versus optional inputs. Instruct the agent to ask for anything missing instead of guessing.

## Program blueprint

TODO: Objective and audience. Message architecture (each touch: purpose, timing, channel, and the job it does). Timing as guidance with reasoning, not rigid rules. Splits and personalization. Exits and suppression. Content blocks described by the job each block does, not fixed copy.

## Klaviyo build mapping

TODO: Flow trigger, profile filters, flow filters, conditional splits, and required catalog or event data. Starting point: Signup form or list-join trigger; flow filter for has not placed order since starting this flow. For tool names, arguments, and API shapes, defer to klaviyo-labs/agent-context and the live Klaviyo API or MCP catalog. Never trust this skill over the live catalog.

## QA

TODO: What "ready to ship" means for this program, as a checklist. The skill guides QA and never sends.

## Measurement

TODO: Primary KPI, guardrail metrics, attribution approach, and holdout guidance. Label every benchmark or example number illustrative unless it cites a verifiable source.

## Worked example

TODO: Add `examples/example-brief.md` with a brief-to-build-spec walkthrough for this program, then point to it here.
