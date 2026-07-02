# Roadmap

This file is the work queue governed by `spec/project/roadmap/`. Each entry is a
level-3 heading followed by a `yaml` code block (`id`, `title`, `detail`,
`outcomes`, `target_sprint`, `mvp`, `status`, in that order) and a free-text
body. `roadmap-plan` and `roadmap-refine` own the detail level and the status
lifecycle. Don't hand-edit those fields here.

Entries carry monotonically increasing IDs starting at `R-1`, never reused.
Outcome IDs (`O-n` in `goals.md`) are an independent counter.

`cookiecutter-gh-project` shipped the minimum-viable-product item below before
adopting the planning suite. This roadmap records it retroactively as
`status: done`, mapped to sprint 1, so the mission's minimum viable product
resolves.

## Phase 1: Standardised project scaffolding

### R-1: Cookiecutter template for nolte-style projects

```yaml
id: R-1
title: Cookiecutter template for nolte-style projects
detail: fine
outcomes: [O-1, O-2]
target_sprint: 1
mvp: true
status: done
```

The `cookiecutter` template that scaffolds a standardised GitHub project,
pre-wired with GitHub Actions and settings based on `gh-plumbing` (release,
`mkdocs`, static tests, labelling). Capability
`github-project-cookiecutter-template` in `project/portfolio.yml`.
