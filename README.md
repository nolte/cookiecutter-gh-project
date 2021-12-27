# Github Project Templates


## Usage

```bash
cookiecutter ./cookiecutter-gh-project \
    module_slug="cookiecutter-gh-project" \
    topics="templating, cookiecutter, github" \
    description="Template for Create Github Workflows and Projects" \
    template_issues="y" \
    template_pull_request="y" \
    plumbing_workflow_enabled="y" \
    plumbing_workflow_source="../sources/cookiecutter-gh-project" \
    dependabot_pip="y" \
    dependabot_gitsubmodule="n" \
    dependabot_docker="n" \
    -f --no-input

cookiecutter gh:nolte/cookiecutter-gh-project \
    module_slug="cookiecutter-gh-project" \
    topics="templating, cookiecutter, github" \
    description="Template for Create Github Workflows and Projects" \
    template_issues="y" \
    template_pull_request="y" \
    dependabot_github_actions="y" \
    dependabot_pip="y" \
    dependabot_gitsubmodule="n" \
    dependabot_docker="n" \
    -f --no-input
```

# init

```
asdf reshim python
```
