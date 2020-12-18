# Template

This Template Project use [Cookiecutter](https://github.com/cookiecutter/cookiecutter) for generate/boostrap Github Projects. With a base set of CI/CD tools and Release Process.

## Scope from the Templates

This Template shoud be handle different base Ci/Cd steps.

### Static Tests

Generate a base set of workflows for execute Static Tests, like linting.

* [pre-commit/action](https://github.com/pre-commit/action)
* [zbeekman/EditorConfig-Action](https://github.com/zbeekman/EditorConfig-Action)

### Release Process

The Release Process will be implemented by different Workflows and Apps, for example [toolmantim/release-drafter](https://github.com/toolmantim/release-drafter) for creating a GitHub Changelog.

#### Release Publish Docs

* [mhausenblas/mkdocs-deploy-gh-pages](https://github.com/mhausenblas/mkdocs-deploy-gh-pages)

### Project Configuration

#### Settings

* [probot/settings](https://github.com/probot/settings)


#### Labeling

* [probot/stale](https://github.com/probot/stale)
* [kaxil/boring-cyborg](https://github.com/kaxil/boring-cyborg)

#### Templates

* [docs.github.com Templates](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository)
