# Usage

For Direct use you will need [Cookiecutter](https://github.com/cookiecutter/cookiecutter),

```sh
pip install cookiecutter
```

After this you can use Template from [nolte/cookiecutter-gh-project](https://github.com/nolte/cookiecutter-gh-project).

```sh
cookiecutter gh:nolte/cookiecutter-gh-project \
    module_slug="my-test-project" \
    topics="templating, cookiecutter, github" \
    description="Template for Create Github Workflows and Projects" \
    template_issues="y" \
    template_pull_request="y" \
    workflow_deliver_docs_enabled="n" \
    dependabot_github_actions="y" \
    dependabot_pip="y" \
    dependabot_gitsubmodule="n" \
    dependabot_docker="n" \
    -f --no-input
```

Generated Folder **Structure** from command.

```sh
my-test-project
├── .github
│   ├── boring-cyborg.yml
│   ├── dependabot.yml
│   ├── ISSUE_TEMPLATE
│   │   ├── bug_report.md
│   │   ├── config.yml
│   │   └── feature_request.md
│   ├── pull_request_template.md
│   ├── release-drafter.yml
│   ├── settings.yml
│   ├── stale.yml
│   └── workflows
│       ├── build-static-tests.yaml
│       ├── release-cd-refresh-master.yml
│       └── release-drafter.yml
└── .pre-commit-config.yaml
```

All Parameters are listed at `./cookiecutter.json`, at the project root.
