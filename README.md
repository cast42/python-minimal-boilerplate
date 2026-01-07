# python-minimal-boilerplate

Modern minimal boilerplate for a Python project with following developer dependencies:

- from [Astral](https://astral.sh):
  - package manager for dependency management: `uv`,
  - linting: `ruff`,
  - type checking: `ty`
- testing: `pytest`, and
- [documentation](https://github.com/cast42/zensical): `zensical`.

It uses command runner [`just`](https://github.com/casey/just) as a handy way to save and run project-specific commands.
Logging is optionally with [Pydantic Logfire](https://pydantic.dev/logfire) as an example, but you can easily switch to your own favorite logger.

## Installation

### Create a new repository starting from the template

Create a new repository from the template. Open the browser at
[https://github.com/cast42/python-minimal-boilerplate](https://github.com/cast42/python-minimal-boilerplate)
and click `Use this template` (Create a new repository). Give your new repository a name. E.g. `new-repo-name-from-template`

Next clone your new repository, generated from the template. Do not forget to replace url with url of the new repository:

```sh
git clone https://github.com/<your github handle>/<new-repo-name-from-template>.git
```

### Install uv if not already installed

- Install `uv` following the upstream instructions: <https://docs.astral.sh/uv/getting-started/installation/>

### Install Just for command invocation

If `just` is not yet installed. Install with (on osx)

```sh
brew install just
```

or on Ubuntu Linux:

```
sudo apt update
sudo apt install just
```

or on other platforms:

[Installation instructions for just on other plafforms](<https://github.com/casey/just?tab=readme-ov-file#installation>)

## Initial setup of the project

Change directory into the new cloned directory (Replace new-repo-from-template with the name of your repository):

```sh
cd new-repo-name-from-template
```

### Optional: Provide logfire token for logging in the eu cloud

If you want to inspect the logging via the logfire project site, you need to provide the logfire token. If no token is provided, no logging is sent to the cloud and only logging is emmited on the command line output.

Get your logfire token (get it here [https://logfire.pydantic.dev/docs/how-to-guides/create-write-tokens/](https://logfire.pydantic.dev/docs/how-to-guides/create-write-tokens/)), copy the .env.example to .env and fill in value for  LOGFIRE_TOKEN.
The app calls `logfire.configure(send_to_logfire='if-token-present')`, so nothing
is sent to Logfire unless you provide credentials.

## Test if everthing works

Check the code quality with ruff and ty from Astral by running the command `just check`:

```sh
> just check
uv run ruff check --fix
All checks passed!
uv run ty check
Checking ------------------------------------------------------------ 2/2
files
All checks passed!
```

Test the code by issuing command `just test`:

```sh
> just test
uv run -m pytest -q
.
1 passed in 0.01s
```

Run the python code in `src/main.py`:

```sh
> just run
```

Since the justfile starts with `set dotenv-load`, the environment variables defined in the `.env` file are loaded before
the python program is run. The python program will also run if the LOGFIRE_TOKEN environment variable is not set but no logging on pydantic endpoint will be done.

You should see this output from running `just run` on the commandline:

```sh
uv run python -m src.main
15:12:23.707 application.startup
Hello from python-minimal-boilerplate!
```

### Customize the Copilot instructions

The template ships with `.vscode/copilot-instructions.md` for GitHub Copilot (or similar AI helpers).
Treat it as a starting point and adapt the contents to your personal style so Copilot mirrors how you like to code.
Update things like your preferred line length, indentation width, naming conventions, or any other guidance that differs from the defaults baked into the file.

### Build documentation

Configure the site name, description and author in [zensical.toml](./zensical.toml):

```toml
[project]
site_name = "your-project-name"
site_description = "Description of your python project"
site_author = "Your Name"
```

Generate the static documentation with zensical:

```sh
just docs
```

The rendered site is written to the `site/` directory.

### View documentation for `src/main.py`

After running `just docs`, view the generated documentation. Zensical extracts docstrings and type information directly from your Python source files, keeping the documentation aligned with the implementation in `src/main.py`.

## Just recipes

Run `just` (or the default alias `just --list`) to see every command that ships with the template:

```sh
> just
Available recipes:
    run

    [docs]
    docs *args

    [lifecycle]
    clean        # Remove temporary files
    install      # Ensure project virtualenv is up to date
    update       # Update dependencies

    [qa]
    check *args
    lint *args
    test *args
    typing *args
```

Each recipe is meant for a specific moment in your workflow:

- `run`: Executes `python -m src.main` with `uv run`. Use this to exercise the main entry point locally once dependencies are synced.
- `docs`: Builds documentation with zensical. Run after updating docstrings to regenerate documentation.
- `clean`: Deletes build and cache artifacts (`.venv`, `.pytest_cache`, `.ruff_cache`, `.uv-cache`, `__pycache__`, `*.egg-info`). Reach for this if tooling behaves strangely or you want a fresh workspace before packaging or committing.
- `install`: Calls `uv sync` to ensure the local virtual environment reflects `pyproject.toml`/`uv.lock`. Use after cloning or when dependencies change.
- `update`: Runs `uv sync --upgrade` to refresh dependencies to their latest allowed versions. Follow up with `just check`/`just test` to confirm upgrades are safe.
- `test`: Invokes `uv run -m pytest -q`. Run it before pushing or whenever you change behavior covered by the test suite.
- `lint`: Runs Ruff with `--fix` so formatting and autofixable lint issues are corrected. Helpful during development to keep style consistent.
- `typing`: Performs type checking with Ty. Use it when changing interfaces or touching typed modules.
- `check`: Convenience wrapper that combines `lint` (without formatting churn beyond Ruff fixes) and `typing`. Ideal for pre-commit validation or CI parity.
