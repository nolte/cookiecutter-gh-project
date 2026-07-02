---
id: F-1
title: Scaffolded standard project
status: done
roadmap_item: R-1
sprint: 1
created: 2026-07-02
ended: 2026-07-02
verifies_sprint_value: acceptance-1
consistency_check:
  performed_at: 2026-07-02
  agent_version: manual-fallback (retroactive; feature-consistency-reviewer not run cross-repo)
  findings:
    - kind: clean
      target: project/features/
      resolution: proceed
      evidence: "project/features/ empty (first decomposition); no feature-to-feature overlap possible."
    - kind: prior-art
      target: the shipped cookiecutter template
      resolution: proceed
      evidence: "The cookiecutter template already scaffolds standardised projects; F-1 documents the scaffold contract, it does not build new template logic."
---

## Description

F-1 is the mission-verifying feature for the shipped
`github-project-cookiecutter-template` capability. The `cookiecutter` template
scaffolds a standardised `nolte`-style GitHub project from one run. The contract
holds when a run produces a project pre-wired with `gh-plumbing`-based GitHub
Actions, settings, and a `mkdocs` site. This holds against the shipped template,
so the retroactive reconciliation records this feature as `done` (issue
`nolte/claude-shared#262`).

## Acceptance criteria

- [x] **acceptance-1** A `cookiecutter` run produces a GitHub project pre-wired
  with `gh-plumbing`-based GitHub Actions, settings, and a `mkdocs` documentation
  site. _(This is the sprint value verifier.)_
- [x] **acceptance-2** The generated project carries the release process, static
  tests, and automatic labelling from the `gh-plumbing` baseline.
- [x] **acceptance-3** The scaffold runs from a single `cookiecutter` invocation
  with no manual post-steps for the standard pieces.

## Test hooks

- **acceptance-1**: a `cookiecutter` run against the template, then inspect the
  generated `.github/` and `mkdocs.yml`; passing.
- **acceptance-2**: inspect the generated workflows and settings; passing.
- **acceptance-3**: a single template run; passing.

## Consistency notes

Retroactive documentation feature: the `cookiecutter` template predates the
planning suite. This feature introduces no new implementation. It exists so the
mission's `verifies_via: F-1:acceptance-1` and sprint 1's `value_statement`
resolve to a real acceptance criterion.

## References

- `project/portfolio.yml` capability `github-project-cookiecutter-template`
- `AUDIENCES.md` audience "Developer scaffolding a new nolte-style GitHub project"
- `README.md` (the generated-project feature list)
