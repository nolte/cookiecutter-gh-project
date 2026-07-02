---
mission_statement: "Cookiecutter-gh-project scaffolds a standardised nolte-style GitHub project, pre-wired with gh-plumbing-based GitHub Actions, settings, and mkdocs documentation, from a single cookiecutter run, so a developer starts a new repository from one consistent baseline."
relevant_outcomes: [O-1, O-2]
audiences:
  - Developer scaffolding a new nolte-style GitHub project
  - "Maintainer (`nolte`)"
verifies_via: F-1:acceptance-1
time_bound:
  kind: mvp_completion
mvp_status: achieved
created: 2026-07-02
revised_at: null
---

## Statement

`cookiecutter-gh-project` scaffolds a standardised `nolte`-style GitHub project,
pre-wired with `gh-plumbing`-based GitHub Actions, settings, and `mkdocs`
documentation, from a single `cookiecutter` run. A developer starts a new
repository from one consistent baseline.

- **Specific**: the statement names *what* (a `cookiecutter` template for
  standardised GitHub projects) and *for whom* (a scaffolding developer and the
  maintainer, resolved in `audiences`).
- **Measurable**: `verifies_via: F-1:acceptance-1`. A `cookiecutter` run produces
  a project with pre-wired GitHub Actions, settings, and a `mkdocs` site.
- **Achievable**: the minimum viable product is the shipped
  `github-project-cookiecutter-template` capability. Roadmap item R-1 carries
  `mvp: true`, `detail: fine`, and `target_sprint: 1`.
- **Relevant**: `relevant_outcomes: [O-1, O-2]`. Each entry resolves to an outcome
  in `project/goals.md`.
- **Time-bound**: `time_bound: { kind: mvp_completion }`. The bound is the moment
  the shipped minimum viable product reaches achieved status.

## Audiences

- **Developer scaffolding a new nolte-style GitHub project**: the minimum viable
  product delivers a `cookiecutter` template that produces a ready project,
  pre-wired with GitHub Actions, settings, and `mkdocs` documentation, from one
  run.
- **Maintainer (`nolte`)**: the minimum viable product delivers one place to hold
  the standard project layout, aligned with the `gh-plumbing` baseline, so every
  new repository starts consistent.

## Verification

Feature **F-1: Scaffolded standard project** verifies the mission through
acceptance criterion 1: *"A `cookiecutter` run produces a GitHub project pre-wired
with `gh-plumbing`-based GitHub Actions, settings, and a `mkdocs` documentation
site."* This is the `verifies_sprint_value` criterion for sprint 0001 and holds
against the shipped template, so the minimum viable product records as
`achieved`.

## Source

- **Audience artefact**: `AUDIENCES.md` at the `cookiecutter-gh-project`
  repository root, consulted at its current develop tip. The two `audiences`
  entries are the scaffolding developer and the maintainer.
- **Outcomes referenced**: O-1, O-2 from `project/goals.md`.
- **Authored by**: the `mission-define` cascade (issue `nolte/claude-shared#262`
  mission-authoring backfill), 2026-07-02. The cascade models the minimum viable
  product retroactively. The template capability already carried `status: active`
  when the repository adopted the planning suite, so the roadmap records R-1 as
  `status: done` and opens `mvp_status` at `achieved`.
