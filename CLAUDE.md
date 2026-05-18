# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template that scaffolds a standardised GitHub project. The generated project consumes reusable GitHub Actions and Probot settings from [`nolte/gh-plumbing`](https://github.com/nolte/gh-plumbing) — so changes here propagate to every downstream repo created from this template.

There is no application code. The "source" is template files; the "tests" are running cookiecutter and inspecting the output.

## Repository layout

- `cookiecutter.json` — template variables and their defaults (e.g. `module_slug`, `docs_enabled`, `template_issues`, `dependabot_*`).
- `{{cookiecutter.module_slug}}/` — the template root. Everything inside is rendered into the generated project.
- Top-level `README.md`, `mkdocs.yml`, `.github/`, `docs/` — describe and ship the template itself, **not** the generated project. Do not confuse them with their counterparts under `{{cookiecutter.module_slug}}/`.
- `test/` — untracked directory used as a scratch output target for local cookiecutter runs.
- `styles/`, `.vale.ini` — Vale prose linting for the template's own docs.

## Two templating layers — escape carefully

Files under `{{cookiecutter.module_slug}}/` pass through Jinja2 (Cookiecutter) first, then — at runtime in the generated repo — through GitHub Actions expression syntax. Both use `{{ }}`. To emit a literal GitHub Actions expression, escape with Jinja string literals:

```yaml
secrets:
  token: {{"${{"}} secrets.GITHUB_TOKEN {{"}}"}}
```

See `{{cookiecutter.module_slug}}/.github/workflows/build-static-tests.yaml` for the canonical pattern.

Conditional file inclusion is encoded in **the filename itself** with whitespace-trimmed Jinja blocks, e.g.:

```
{%- if cookiecutter.docs_enabled == "y" -%}mkdocs.yml{%- endif -%}
```

When the condition is false the filename renders empty and Cookiecutter drops the file. Preserve this exact spelling (including the `-` whitespace trim markers) when adding new conditional artefacts.

## Common commands

Generate the template into `/tmp` (the canonical development invocation, mirroring `README.md`):

```bash
cookiecutter ./cookiecutter-gh-project \
    module_slug="cookiecutter-gh-project" \
    topics="templating, cookiecutter, github" \
    description="Template for Create GitHub Workflows and Projects" \
    template_issues="y" \
    template_pull_request="y" \
    plumbing_workflow_enabled="y" \
    plumbing_workflow_source="../sources/cookiecutter-gh-project" \
    dependabot_pip="y" \
    -f --no-input --output-dir /tmp
```

Note `cookiecutter` resolves the template path relative to the parent directory — run from one level up, or pass an absolute path.

Other:

- `pip install -r requirements.txt -r requirements-dev.txt` — install cookiecutter + mkdocs toolchain.
- `pre-commit run --all-files` — same hooks CI runs (`check-yaml` is excluded for the template tree because raw Jinja is not valid YAML).
- `mkdocs serve` / `mkdocs build` — preview the template's own documentation site.
- `task` — lists available tasks; concrete targets live in remote includes from `nolte/taskfiles` (mkdocs, pre-commit).
- Python version is pinned via `.tool-versions` (`python 3.14.0`, asdf-style).

## CI and lifecycle

- `.github/workflows/build-static-tests.yaml` — pre-commit + Trivy via reusable workflows from `nolte/gh-plumbing@v1.1.12`. The pin must be a tag, not a branch.
- `.github/workflows/lifecycle-update-boilerplate-code.yaml` — manual `workflow_dispatch` that re-runs cookiecutter against itself and opens/updates a `lifecycle/boilerplate-update` PR into `develop`. Editing this workflow affects the self-update loop.
- `.github/workflows/release-drafter.yml` + `release-cd-*` — release-drafter assembles notes; CD jobs publish docs and refresh `master`.
- Default branch is `develop`; releases are merged to `master`.

## When changing the template

1. Edit files under `{{cookiecutter.module_slug}}/`.
2. Regenerate into `test/` or `/tmp` with the development command above.
3. Diff the regenerated output against a previous generation to verify the effect of your change — there is no unit-test harness; visual diff of the output **is** the verification step.
4. If you add a new variable, add it to `cookiecutter.json` with a sensible default and document the option in `README.md` / `docs/usage.md`.
