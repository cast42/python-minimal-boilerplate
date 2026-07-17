---
name: minimal-python-boilerplate
description: Turn this minimal uv-based boilerplate into a named, working Python application or library. Use when starting a Python project from the template, replacing placeholder metadata and example code, choosing a package layout or entry point, adding initial dependencies, or aligning tests, documentation, and developer commands with a new project's requirements.
---

# Create a Python Project

Adapt the existing repository instead of rebuilding its tooling from scratch. Keep only the features the requested project needs.

## 1. Inspect the template

- Read `AGENTS.md`, `README.md`, `pyproject.toml`, `justfile`, `zensical.toml`, `src/`, and `tests/`.
- Check `git status` and preserve unrelated user changes.
- Confirm `uv` and `just` are available before relying on them.
- Identify the requested project name, purpose, Python version, application or library shape, entry points, dependencies, logging, and documentation needs. Infer low-risk details from the request and ask only when a choice materially changes the result.

## 2. Define names consistently

Derive and use these distinct forms:

- Distribution name: lowercase kebab-case for `[project].name`.
- Import package: lowercase snake_case below `src/`.
- Command name: a short kebab-case key below `[project.scripts]`, if a CLI is needed.
- Human name and description: readable values for the README and documentation site.

Search for template names and placeholders before editing. Rename files and update imports, tests, scripts, documentation, and configuration together. Do not leave both the example package and its replacement.

## 3. Shape the project

- Keep the `src` layout and place importable code in `src/<package_name>/`.
- Remove `src/main.py` when the package entry point supersedes it; otherwise make the `just run` recipe and documentation match the chosen entry point.
- Keep `__init__.py` small. Put behavior in focused modules and expose only the intended public API.
- For a CLI, provide a typed `main()` and map `[project.scripts]` to it.
- For a library, remove the example CLI and project script unless requested.
- Replace example tests with tests of the initial public behavior.
- Use concise docstrings and full type hints for public code.

## 4. Configure tooling

- Update project metadata, `requires-python`, dependencies, scripts, and tool target versions in `pyproject.toml`.
- Add runtime dependencies with `uv add <package>` and developer dependencies with `uv add --dev <package>` so `pyproject.toml` and `uv.lock` stay aligned.
- Retain Ruff, Ty, pytest, pre-commit, and the `justfile` recipes unless the user asks for a different toolchain.
- Keep `just install`, `just check`, `just test`, `just run`, and `just docs` accurate for the resulting project. Remove recipes for deliberately omitted features.
- Treat Logfire as optional example functionality. Remove it and its environment instructions when observability is not requested. If retained, configure it to avoid remote export without an explicit token. Do not claim Azure telemetry support.
- Update `zensical.toml` and `docs/` when documentation is retained. Remove the documentation dependency and recipe together if the user excludes docs.
- Update `.env.example`, ignore rules, CI, and pre-commit configuration when the new setup requires it.

## 5. Rewrite user-facing documentation

Replace template-oriented README text with project-specific content:

- purpose and current scope;
- prerequisites and installation;
- configuration, without real secrets;
- common `just` commands;
- usage examples that match the actual API or CLI;
- testing and documentation commands.

Do not leave instructions about creating a repository from the template after the project has been instantiated.

## 6. Synchronize and verify

Run the narrowest useful checks while editing, then finish with:

```sh
just install
just check
just test
```

Run `just docs` when documentation is present and affected. Run `just run` or invoke the public API for a small smoke test when applicable. Inspect `git diff --check`, `git status`, and the final diff for stale names, placeholders, generated artifacts, or accidental unrelated changes.

If a command cannot run, explain the exact limitation and leave the repository in a coherent state. Summarize the project choices, changed files, validation results, and any decisions still needed from the user.
