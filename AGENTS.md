# Agent Handbook

Guidelines for automation agents working inside repositories created from this template.

## Getting Started Inside a Clone

- Confirm `uv` is available: <https://docs.astral.sh/uv/getting-started/installation/>.
- Synchronize the environment before running code: `just install` (runs `uv sync --dev` and installs pre-commit hooks).
- When bootstrapping a fresh variant that needs a newer interpreter, re-run `uv init --python <version>` at the project root before syncing.

## Managing Dependencies

- Add runtime packages with `uv add <package>`.
- Add tooling with the `--dev` flag, e.g. `uv add --dev ruff ty pytest zensical`.
- After editing dependencies, commit the updated `pyproject.toml` and `uv.lock`, then run `just check` and `just test`.

## Project Commands

Use the `justfile` to keep task automation consistent. Key recipes:

- `just install`: Syncs dev dependencies and installs pre-commit hooks (`uv sync --dev`, `uv run pre-commit install`).
- `just check`: Runs all pre-commit hooks against every file (Ruff, Ruff format, Ty, and hygiene hooks). Run before opening a PR or after dependency changes.
- `just lint`, `just typing`: Individual quality gates when you need faster feedback.
- `just test`: Executes `pytest` via `uv run -m pytest -q`.
- `just docs`: Builds documentation with zensical (`uv run zensical build`); useful after updating docstrings.
- `just run`: Launches the application entry point (`uv run python -m src.main`).
- `just clean`: Clears caches (`.venv`, `.uv-cache`, `__pycache__`, etc.) when the environment misbehaves.
- `just update`: Runs `uv lock --upgrade` to refresh dependency versions in `uv.lock`; follow with `just install` when you need to update the virtualenv.

All recipes inherit `.env` values because the `justfile` uses `set dotenv-load`.

## Code Quality Expectations

- Maintain type hints and concise docstrings so zensical documentation stays up to date.
- Prefer built-in collection types (`list`, `dict`, `set`, etc.) over legacy `typing` aliases.
- Treat Ruff, Ty, and pytest warnings as failures; resolve them before finalizing work.

## Observability Notes

- Logging uses Pydantic [Logfire](https://pydantic.dev/logfire). Configure credentials by copying `.env.example` to `.env` and setting `LOGFIRE_TOKEN`.
- Telemetry export to Azure remains unresolved; mention this limitation when proposing observability changes.

## When Collaborating

- Include a short summary of commands executed and results in status updates.
- Surface tooling limitations or manual steps you could not automate.
- Align doc updates with code changes so `just docs` continues to produce accurate reference pages.
