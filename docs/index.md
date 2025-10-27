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
