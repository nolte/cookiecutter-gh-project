"""Pre-generation hook: validate user-supplied cookiecutter variables.

Runs before any template file is rendered. A non-zero exit aborts the
render with a clear diagnostic — preferable to producing a broken
project tree the user then has to debug.
"""

from __future__ import annotations

import re
import sys

MODULE_SLUG = "{{ cookiecutter.module_slug }}"

SLUG_REGEX = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def _fail(message: str) -> None:
    sys.stderr.write(f"ERROR: {message}\n")
    sys.exit(1)


def validate_module_slug() -> None:
    if not MODULE_SLUG:
        _fail(
            "module_slug is required and must be non-empty. "
            "Pass module_slug=<your-project-slug> on the command line."
        )
    if not SLUG_REGEX.match(MODULE_SLUG):
        _fail(
            f"module_slug '{MODULE_SLUG}' is invalid. "
            "Must match ^[a-z0-9][a-z0-9-]*$ — lowercase ASCII letters, "
            "digits, and hyphens only; first character must be a letter or digit. "
            "Used directly as the GitHub repository name, MkDocs site URL slug, "
            "and Python-friendly identifier."
        )


if __name__ == "__main__":
    validate_module_slug()
