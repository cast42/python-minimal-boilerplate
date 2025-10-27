# python-minimal-boilerplate

Modern minimal boilerplate for a Python project with developer dependencies uv, rust, ty, pytest.
It uses just as a handy way to save and run project-specific commands.
Logging is with [Pydantic Logfire](https://pydantic.dev/logfire) (but you can easily switch to loguru).

## Installation

### Create new repository starting from the template

Create a new repository from the template. Open the browser at
[https://github.com/cast42/python-minimal-boilerplate](https://github.com/cast42/python-minimal-boilerplate)
and click `Use this template` (Create a new repository). Give your new repository a name. E.g. `new-repo-from-template`

Next clone your new repository, generated from the template. Do not forget to replace url with url of the new repositry:

```sh
git clone https://github.com/cast42/new-repo-from-template.git
```

### Install uv if not already installed

- Install `uv` following the upstream instructions: <https://docs.astral.sh/uv/getting-started/installation/>

### Initialise the project

Change directory into the new cloned directory (Replace new-repo-from-template with the name of your repository):

```sh
cd new-repo-from-template
uv init --python 3.14
```

### Add development tools

```sh
uv add --dev ruff ty pytest
```

### Optional: Install logfire for logging

```sh
uv add logfire
```

Get your logfire token, copy the .env.example to .env and fill in value for  LOGFIRE.

### Install Just for command invocation

```sh
brew install just
```

## Test if everthing works

Check the code with ruff and ty from Astral:

```sh
just check
uv run ruff check --fix 
All checks passed!
uv run ty check 
Checking ------------------------------------------------------------ 2/2 files                                                                   All checks passed!
```

Test the code:

```sh
just test
uv run -m pytest -q 
.                                                                                                                                          [100%]
1 passed in 0.02s
```

Run the python code in main.py:

```sh
just run
```

Since the justfile starts with `set dotenv-load` , the environment variables defined in the `.env` file are loaded before
the python program is run. The python program will also run if the LOGFIRE environment variable is not set but no logging on pydantic endpoint will be done.

You should see this:

```sh
uv run python main.py
15:12:23.707 application.startup
Hello from python-minimal-boilerplate!
```

## Available recipies in the just file

```sh
> just
Available recipes:
    run

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
