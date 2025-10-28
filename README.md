# python-minimal-boilerplate

Modern minimal boilerplate for a Python project with following developer dependencies:

- from Astral
  - package manager for dependency management: `uv`,
  - linting: `rust`,
  - type checking: `ty`
- testing: `pytest`, and
- documentation:`mkdocs`.

It uses command runner `just` as a handy way to save and run project-specific commands.
Logging is with [Pydantic Logfire](https://pydantic.dev/logfire) as an exampe, but you can easily switch to your own favorite logger.

## Installation

### Create a new repository starting from the template

Create a new repository from the template. Open the browser at
[https://github.com/cast42/python-minimal-boilerplate](https://github.com/cast42/python-minimal-boilerplate)
and click `Use this template` (Create a new repository). Give your new repository a name. E.g. `new-repo-from-template`

Next clone your new repository, generated from the template. Do not forget to replace url with url of the new repository:

```sh
git clone https://github.com/cast42/new-repo-from-template.git
```

### Install uv if not already installed

- Install `uv` following the upstream instructions: <https://docs.astral.sh/uv/getting-started/installation/>

## Initial setup of the project

Change directory into the new cloned directory (Replace new-repo-from-template with the name of your repository):

```sh
cd new-repo-from-template
```

### Add development tools

```sh
uv add --dev ruff ty pytest mkdocs
```

### Optional: Install logfire for logging

```sh
uv add logfire
```

Get your logfire token, copy the .env.example to .env and fill in value for  LOGFIRE.
The app calls `logfire.configure(send_to_logfire='if-token-present')`, so nothing
is sent to Logfire unless you provide credentials.

### Install Just for command invocation

If `just` is not yet installed. install with (on osx)

```sh
brew install just
```

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
the python program is run. The python program will also run if the LOGFIRE environment variable is not set but no logging on pydantic endpoint will be done.

You should see this output:

```sh
uv run python -m src.main
15:12:23.707 application.startup
Hello from python-minimal-boilerplate!
```

### Build documentation

Generate the static site with MkDocs:

```sh
just docs
```

The rendered site is written to the `site/` directory.

### View documentation for `src/main.py`

After running `just docs` (or `uv run mkdocs serve` for live reload), open `site/index.html` in a browser. The landing page includes an *Application Entry Point (`src/main.py`)* section that explains how the module configures Logfire and what `main()` does. This keeps the narrative documentation aligned with the implementation in `src/main.py`.

## Available recipies in the just file

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
