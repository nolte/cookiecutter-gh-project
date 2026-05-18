"""Post-generation hook: prune files/directories that the user opted out of.

Runs in the freshly-rendered project directory. Replaces the older
"conditional-filename" pattern (Jinja braces inside file names that
collapsed the path to empty when the flag was off): every optional
artifact is now rendered unconditionally and removed here when its
enabling flag is not "y".

Trade-off: the optional files exist on disk for a moment before being
removed. That moment costs nothing and is far outweighed by the
readability gain in the template tree (no more Jinja braces inside file
names, normal git diffs).
"""

from __future__ import annotations

import shutil
from pathlib import Path

PROJECT_ROOT = Path.cwd()

# Each entry: (cookiecutter flag value after Jinja render, paths to remove when
# the flag is not "y"). Must be a list of tuples, not a dict — Cookiecutter
# renders this file through Jinja2 before executing it, so each flag reference
# below collapses to a literal "y" or "n" at render time. With a dict, every
# "n"-keyed entry would collapse to a single mapping (last one wins).
REMOVE_WHEN_DISABLED: list[tuple[str, list[str]]] = [
    ("{{ cookiecutter.readme_enabled }}", ["README.md"]),
    (
        "{{ cookiecutter.docs_enabled }}",
        ["docs", "mkdocs.yml", "requirements-dev.txt"],
    ),
    ("{{ cookiecutter.renovate_enabled }}", ["renovate.json5"]),
    ("{{ cookiecutter.dependabot_enabled }}", [".github/dependabot.yml"]),
    ("{{ cookiecutter.template_issues }}", [".github/ISSUE_TEMPLATE"]),
    (
        "{{ cookiecutter.template_pull_request }}",
        [".github/pull_request_template.md"],
    ),
    (
        "{{ cookiecutter.plumbing_workflow_enabled }}",
        [".github/workflows/lifecycle-update-boilerplate-code.yaml"],
    ),
]


def _remove(rel_path: str) -> None:
    target = PROJECT_ROOT / rel_path
    if not target.exists():
        return
    if target.is_dir():
        shutil.rmtree(target)
    else:
        target.unlink()


def prune_disabled_artifacts() -> None:
    for flag_value, rel_paths in REMOVE_WHEN_DISABLED:
        if flag_value == "y":
            continue
        for rel_path in rel_paths:
            _remove(rel_path)


if __name__ == "__main__":
    prune_disabled_artifacts()
