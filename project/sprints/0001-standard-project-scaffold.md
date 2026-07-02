---
number: 1
status: closed
started: 2026-07-02
ended: 2026-07-02
value_statement: A developer scaffolds a standardised nolte-style GitHub project, pre-wired with gh-plumbing-based Actions, settings, and mkdocs docs, from a single cookiecutter run.
artifact_ref: develop (shipped capability, pre-planning-suite)
roadmap_items: [R-1]
features: [F-1]
---

## Goal

A developer runs the `cookiecutter` template and obtains a standardised GitHub
project, pre-wired with `gh-plumbing`-based GitHub Actions, settings, and a
`mkdocs` site. Success is verified by F-1 `acceptance-1`: a run produces a project
carrying those pre-wired pieces.

## Features

- [F-1](../features/scaffolded-standard-project.md): Scaffolded standard project, status: done

## Out of scope

- The `gh-plumbing` reusable workflows and Probot commons themselves, which the
  generated project consumes but which live in their own repository.
- Per-project content beyond the standard scaffold.

## Review notes

Retroactive reconciliation (2026-07-02): the
`github-project-cookiecutter-template` capability already carried `status: active`
before this repository adopted the planning suite (issue `nolte/claude-shared#262`
mission-authoring backfill). This sprint records roadmap item R-1 and feature F-1
as `done`, and itself as `closed`, to document the delivered minimum viable
product rather than to plan new work.
