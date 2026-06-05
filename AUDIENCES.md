# Audiences — GitHub Project Cookiecutter Template

<!--
Produced following spec/project/audience-identification/. Audiences are derived
from the repository's README and purpose, not invented. Do not add audiences
without first declaring the bounded context.
-->

## Bounded context

A Cookiecutter template that scaffolds a standardised nolte-style GitHub
project, pre-wired with GitHub Actions and settings based on nolte/gh-plumbing
plus an MkDocs documentation setup, from a single cookiecutter run.

**Inside the boundary**

- The Cookiecutter template tree (`{{cookiecutter.module_slug}}/`)
- `cookiecutter.json` and the generation `hooks/`

**Outside the boundary**

- Cookiecutter itself
- The generated downstream projects
- `nolte/gh-plumbing` (whose workflows and settings the generated project adopts)

## Audiences

Each entry: label, relationship category, interaction surface, expectation,
documentation `track` (per spec/project/docs-audience-tracks/), status, criticality.

### Direct consumers

- **Developer scaffolding a new nolte-style GitHub project** — _category_: direct-consumer ·
  _surface_: the `cookiecutter` run, the `cookiecutter.json` prompts, the generated project ·
  _expects_: a standardised project with gh-plumbing CI/settings, MkDocs docs, a release process, and labelling ·
  _track_: `user-docs` · _status_: `assumed` · _criticality_: primary

### Contributors / maintainers

- **Maintainer (`nolte`)** — _category_: contributor ·
  _surface_: the template source, the generation hooks, CI ·
  _expects_: a template that renders a passing project and green CI ·
  _track_: `developer-docs` · _status_: `assumed` · _criticality_: primary
- **Claude Code as co-author** — _category_: contributor ·
  _surface_: `CLAUDE.md`, `.claude/`, the Taskfile ·
  _expects_: deterministic conventions ·
  _track_: `developer-docs` · _status_: `assumed` · _criticality_: secondary

### Governing parties

- **nolte portfolio conventions (gh-plumbing baseline)** — _category_: governing ·
  _surface_: the gh-plumbing workflows/settings the generated project inherits ·
  _expects_: generated projects stay aligned with the portfolio baseline ·
  _track_: `developer-docs` · _status_: `assumed` · _criticality_: secondary

## Revisit triggers

Re-run `audience-identify revisit` when any of the following changes:

- The gh-plumbing baseline the template targets changes materially.
- The template gains a second project archetype.
