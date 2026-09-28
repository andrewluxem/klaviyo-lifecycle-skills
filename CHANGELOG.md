# Changelog

All notable changes to this project are recorded here. Dates are YYYY-MM-DD.

## [0.1.0] - 2026-09-28

### Added

- Repo scaffold: README, MIT license, contributing guide, roadmap, and this changelog.
- `skills/_template/`: a fully annotated authoring template with reference files, an example validation script, and an example brief.
- Stub folders for nine skills: `welcome-series`, `abandonment-recovery`, `post-purchase`, `winback-reactivation`, `replenishment`, `sunset-suppression`, `pre-send-qa`, `brief-to-build`, and `program-scorer`. Each stub has valid frontmatter and TODO markers for every required section.
- `tests/test_skills.py`: a dependency-free smoke test that validates every skill folder.
- `.github/workflows/skill-tests.yml`: runs the smoke test on every push and pull request.
