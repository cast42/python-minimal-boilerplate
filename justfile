#!/usr/bin/env just --justfile
export PATH := join(justfile_directory(), ".env", "bin") + ":" + env_var('PATH')

set dotenv-load

@_:
    just --list

[group('qa')]
test *args:
    uv run -m pytest -q {{args}}

[group('qa')]
lint *args:
    uv run ruff check --fix {{args}}

[group('qa')]
typing *args:
    uv run ty check {{args}}

[group('qa')]
check *args:
    # Run pre-commit hooks against all files
    uv run pre-commit run --all-files

[group('docs')]
docs *args:
    uv run zensical build {{args}}

run:
    uv run python -m src.main

# Remove temporary files
[group('lifecycle')]
clean:
    rm -rf .venv .pytest_cache .ruff_cache .uv-cache
    find . -type d -name "*.egg-info" -exec rm -rf {} +
    find . -type d -name "__pycache__" -exec rm -r {} +

# Update dependencies
[group('lifecycle')]
update:
    # Upgrade all dependencies in the lock file but leave the .venv
    uv lock --upgrade

# Ensure project virtualenv is up to date
[group('lifecycle')]
install:
    uv sync --dev
    uv run pre-commit install
