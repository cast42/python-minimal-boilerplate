# Python Minimal Boilerplate

Welcome to the documentation for the minimal Python boilerplate project.

## Overview

This template ships with:

- Dependency management via [uv](https://docs.astral.sh/uv/)
- Automation using [`just`](https://github.com/casey/just)
- Quality gates powered by Ruff, Ty, and pytest
- Structured logging delivered through [Pydantic Logfire](https://pydantic.dev/logfire)

## Getting Started

Use the `just` recipes to lint, type-check, test, and build project documentation:

```sh
just check   # lint + type-check
just test    # run the pytest suite
just docs    # build MkDocs documentation into the site/ directory
```

## Application Entry Point (`src/main.py`)

The application’s main module lives at `src/main.py`. It configures Logfire with `send_to_logfire='if-token-present'`, so nothing leaves your machine unless a token is configured, and exposes a `main()` function that emits a structured startup log and prints the greeting. Run `just run` (or `uv run python -m src.main`) to exercise the entry point. The same behaviour is documented here so MkDocs keeps the landing page in sync with the code.
