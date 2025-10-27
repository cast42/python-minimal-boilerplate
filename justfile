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
    cd azure-function; uv run ty check {{args}}

[group('qa')]
check *args:
    uv run ruff check --fix {{args}}
    uv run ty check {{args}}

[group('docs')]
docs *args:
    uv run mkdocs build {{args}}

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
    uv sync --upgrade

# Ensure project virtualenv is up to date
[group('lifecycle')]
install:
    uv sync
