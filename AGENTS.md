# Agent Instructions

- Read the repository before changing it. Preserve user changes and keep the setup minimal.
- Use `.agents/skills/minimal-python-boilerplate/SKILL.md` when creating a Python project from this template or changing its project setup.
- Manage environments and dependencies with `uv`; use `uv add` instead of editing resolved dependency files by hand.
- Use the `justfile` recipes as the project interface. Run `just install` after dependency changes.
- Keep Python code typed and documented. Prefer built-in collection types such as `list` and `dict`.
- Before finishing, run `just check` and `just test`. Run `just docs` when code or documentation changes affect the generated reference.
- Report the files changed, checks run, and any remaining manual work.
