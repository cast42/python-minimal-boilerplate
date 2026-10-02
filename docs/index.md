# Python Minimal Boilerplate

Welcome to the documentation for the minimal Python boilerplate project.

## Overview

This template ships with:

- Dependency management via [uv](https://docs.astral.sh/uv/)
- Automation using [`just`](https://github.com/casey/just)
- Quality gates powered by Ruff, Ty, and pytest
- Supply chain safeguards through `uv audit` and the `pyproject.toml` `exclude-newer = "7 days"` default cooldown. Ruff, Zensical, and the uv build backend have explicit cooldown exceptions for the latest release update
- Structured logging delivered through [Pydantic Logfire](https://pydantic.dev/logfire)

## Getting Started

Use the `just` recipes to lint, type-check, test, and build project documentation:

```sh
just install # sync dependencies and install pre-commit hooks
just check   # run pre-commit checks
just test    # run the pytest suite
just docs    # build documentation and fail on warnings
just docs-serve # preview documentation at http://localhost:8000
```

## Agentic Files

The template includes agent-facing files so coding agents can adapt the project without losing the repository conventions.

- `AGENTS.md` contains the shared repository rules for agents. It covers reading before editing, preserving user changes, using `uv` and `just`, keeping Python typed and documented, and running the expected checks before finishing.
- `.claude/CLAUDE.md` is a small Claude-specific adapter. It points Claude back to `AGENTS.md` and tells it to use the same project skill as other agents.
- `.agents/skills/minimal-python-boilerplate/SKILL.md` contains the full workflow for turning this template into a named Python application or library. It covers naming, package layout, dependencies, entry points, tests, documentation, and final verification.

On Windows checkouts where symlinks are disabled, `.claude/skills` can appear as a plain file instead of a directory. In that case, agents should read the skill directly from `.agents/skills/minimal-python-boilerplate/SKILL.md`.

## Application Entry Point

The CLI entry point lives at `src/python_minimal_boilerplate/cli.py`. It configures Logfire with `send_to_logfire='if-token-present'`, so nothing leaves your machine unless a token is configured, and exposes a `main()` function that emits a structured startup log and prints the greeting. Run `just run` (or `uv run python-minimal-boilerplate`) to exercise the entry point.

See [the CLI reference][python_minimal_boilerplate.cli.main] for its signature and source code.

## Public Helpers

The [greeting helper][python_minimal_boilerplate.main.greeting] returns a greeting for a supplied name:

```python
from python_minimal_boilerplate.main import greeting

assert greeting("Ada") == "Hello, Ada"
```

## Documentation

[Zensical](https://zensical.org/) builds the site from `docs/` and `zensical.toml`.
Its built-in `api-autonav` support discovers the package in `src/` and creates the
API Reference navigation section. Adding a public module adds a reference page
on the next build without needing to maintain a separate Markdown directive.

Python signatures, docstrings, and source listings are rendered through
`mkdocstrings-python`, which is still required. MkDocs remains an indirect
dependency of mkdocstrings. The project uses Zensical to build and preview the
site. See [Zensical's plugin compatibility guide](https://zensical.org/docs/compatibility/mkdocs/plugins/)
for supported replacements.

Run `just docs --clean` after a Zensical upgrade to clear the build cache. The
build checks internal links and anchors, and `just docs` fails on warnings.
Run `just docs-serve` to browse the site locally with automatic reload.

Before publishing, set `site_url` in `zensical.toml` to your deployment URL.
You can then add `navigation.instant` to the theme features. Instant navigation
requires that URL and is disabled in the template.
