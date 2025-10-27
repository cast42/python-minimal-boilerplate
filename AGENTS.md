# Agent Handbook

## Environment Setup

- Install `uv` following the upstream instructions: <https://docs.astral.sh/uv/getting-started/installation/>
- Initialize each project with the newest available Python interpreter, e.g.:

```sh
uv init --python 3.14
```

## Dependency Management

- Add runtime dependencies with `uv add`, for example `uv add logfire`.
- Add development-only tooling with the `--dev` flag, e.g. `uv add --dev ruff`.
- Install MkDocs for documentation with `uv add --dev mkdocs`.

## Code Quality Standards

- Lint with Ruff, check types with Ty, and test with pytest. All three can be installed via:

```sh
uv add --dev ruff ty pytest
```

- Prefer builtin collection types (`list`, `dict`, etc.) over legacy aliases from `typing`.
- Keep typing annotations up to date and provide function docstrings so MkDocs can render documentation.

## Observability

- Experiment with [logfire](https://pydantic.dev/logfire) from Pydantic for logging.
- Telemetry routing to Azure is still unresolved; note this limitation in proposals or status updates.

## Command Automation

- Use the project `justfile` to run repeatable commands.
- Install `just` via <https://github.com/casey/just/blob/master/README.md> if it is not already available.
- Add `set dotenv-load` to make commands inherit environment variables from `.env`.
- Conventionally:
  - `just check` combines linting and type checking.
  - `just test` executes the test suite in the `tests` directory.
  - `just docs` builds the MkDocs site into `site/`.
