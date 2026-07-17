# Python Minimal Boilerplate

Welcome to the documentation for the minimal Python boilerplate project.

## Overview

This template ships with:

- Dependency management via [uv](https://docs.astral.sh/uv/)
- Automation using [`just`](https://github.com/casey/just)
- Quality gates powered by Ruff, Ty, and pytest
- Supply chain safeguards through `uv audit` and the `pyproject.toml` `exclude-newer = "7 days"` cooldown, which help detect known vulnerable dependencies and avoid newly published packages until they have had time to settle
- Structured logging delivered through [Pydantic Logfire](https://pydantic.dev/logfire)

## Getting Started

Use the `just` recipes to lint, type-check, test, and build project documentation:

```sh
just check   # run pre-commit checks
just test    # run the pytest suite
just docs    # build documentation with zensical and mkdocstrings zensical plugin
```

## Agentic Files

The template includes agent-facing files so coding agents can adapt the project without losing the repository conventions.

- `AGENTS.md` contains the shared repository rules for agents. It covers reading before editing, preserving user changes, using `uv` and `just`, keeping Python typed and documented, and running the expected checks before finishing.
- `.claude/CLAUDE.md` is a small Claude-specific adapter. It points Claude back to `AGENTS.md` and tells it to use the same project skill as other agents.
- `.agents/skills/minimal-python-boilerplate/SKILL.md` contains the full workflow for turning this template into a named Python application or library. It covers naming, package layout, dependencies, entry points, tests, documentation, and final verification.

On Windows checkouts where symlinks are disabled, `.claude/skills` can appear as a plain file instead of a directory. In that case, agents should read the skill directly from `.agents/skills/minimal-python-boilerplate/SKILL.md`.

## Application Entry Point

The CLI entry point lives at `src/python_minimal_boilerplate/cli.py`. It configures Logfire with `send_to_logfire='if-token-present'`, so nothing leaves your machine unless a token is configured, and exposes a `main()` function that emits a structured startup log and prints the greeting. Run `just run` (or `uv run python-minimal-boilerplate`) to exercise the entry point.

::: python_minimal_boilerplate.cli
    handler: python
    options:
      members:
        - main
      show_root_heading: false
      show_source: true

## Public Helpers

The package also includes a small public helper module used by the test suite and generated reference documentation.

::: python_minimal_boilerplate.main
    handler: python
    options:
      members:
        - greeting
      show_root_heading: false
      show_source: true
