# GitHub Project Templates

[![GitHub Project Stars](https://img.shields.io/github/stars/nolte/cookiecutter-gh-project.svg?label=Stars&style=social)](https://github.com/nolte/cookiecutter-gh-project) [![GitHub Issue Tracking](https://img.shields.io/github/issues-raw/nolte/cookiecutter-gh-project.svg)](https://github.com/nolte/cookiecutter-gh-project) [![GitHub LatestRelease](https://img.shields.io/github/release/nolte/cookiecutter-gh-project.svg)](https://github.com/nolte/cookiecutter-gh-project) [![.github/workflows/build-static-tests.yaml](https://github.com/nolte/cookiecutter-gh-project/actions/workflows/build-static-tests.yaml/badge.svg)](https://github.com/nolte/cookiecutter-gh-project/actions/workflows/build-static-tests.yaml) [![.github/workflows/release-cd-deliver-docs.yml](https://github.com/nolte/cookiecutter-gh-project/actions/workflows/release-cd-deliver-docs.yml/badge.svg)](https://github.com/nolte/cookiecutter-gh-project/actions/workflows/release-cd-deliver-docs.yml)

---
<!--intro-start-->
This project is intended to help create GitHub structures that are as standardised as possible.

The Generated Project has:

* Pre-configured GitHub Actions and Settings based on [nolte/gh-plumbing](https://github.com/nolte/gh-plumbing).
    * [Release Process](https://nolte.github.io/gh-plumbing/features/release/)
    * [Publishing Documentation](https://nolte.github.io/gh-plumbing/features/mkdocs/)
    * Minimal set of [static tests](https://nolte.github.io/gh-plumbing/features/static-tests/)
    * Automatic [labelling](https://nolte.github.io/gh-plumbing/features/labelling/)
* Documentation with [mkdocs](https://github.com/mkdocs/mkdocs)
<!--intro-end-->

## Usage

Using [cookiecutter/cookiecutter](https://github.com/cookiecutter/cookiecutter) directly for generate a new GitHub Project Structure.

<!--usage-cmd-start-->
```sh
cookiecutter gh:nolte/cookiecutter-gh-project \
    module_slug="cookiecutter-gh-project" \
    topics="templating, cookiecutter, github" \
    description="Template for Create GitHub Workflows and Projects" \
    template_issues="y" \
    template_pull_request="y" \
    readme_enabled="y" \
    docs_enabled="y" \
    renovate_enabled="y" \
    -f --no-input
```
<!--usage-cmd-end-->


## Development


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
    dependabot_gitsubmodule="n" \
    dependabot_docker="n" \
    -f --no-input --output-dir /tmp
```

## Links

* [nolte/taskfiles](https://github.com/nolte/taskfiles), as task collection.
* [nolte/gh-plumbing](https://github.com/nolte/gh-plumbing), for central managed GitHub actions.
