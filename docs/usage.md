# Usage


## Create Project

command for **generate** new Project,

{%
   include-markdown "../README.md"
   start="<!--usage-cmd-start-->"
   end="<!--usage-cmd-end-->"
%}


### Generated structure

```sh
.
├── docs
│   ├── css
│   │   └── overwrite.css
│   └── index.md
├── .github
│   ├── boring-cyborg.yml
│   ├── ISSUE_TEMPLATE
│   │   ├── bug_report.md
│   │   ├── config.yml
│   │   └── feature_request.md
│   ├── pull_request_template.md
│   ├── release-drafter.yml
│   ├── settings.yml
│   ├── stale.yml
│   └── workflows
│       ├── automerge.yaml
│       ├── build-static-tests.yaml
│       ├── release-cd-deliver-docs.yml
│       ├── release-cd-refresh-master.yml
│       ├── release-drafter.yml
│       └── spelling.yaml
├── .gitignore
├── mkdocs.yml
├── .pre-commit-config.yaml
├── README.md
├── renovate.json5
├── requirements-dev.txt
└── .vale.ini

5 directories, 23 files
```
