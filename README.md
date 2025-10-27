# python-minimal-boilerplate

Modern minimal boilerplate for a Python project with uv, rust, ty, pytest and just.

## Installation

Clone this repo:

```sh
git clone https://github.com/cast42/python-minimal-boilerplate.git
```

### Install uv if not already installed

- Install `uv` following the upstream instructions: <https://docs.astral.sh/uv/getting-started/installation/>

### Initialise the project

```sh
cd python-minimal-boilerplate
uv init --python 3.14
```

### Add development tools

```sh
uv add --dev ruff ty pytest
```

### Install logfire for logging

```sh
uv add logfire
```

### Install Just for command invocation

```sh
brew install just
```

## Test if everthing works

Run the command:

```sh
just run
```

You should see this:

```sh
uv run python main.py
Using CPython 3.14.0
Creating virtual environment at: .venv
Hello from python-minimal-boilerplate!
```
