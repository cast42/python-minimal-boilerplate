# Python Coding Conventions

## Python Instructions

- Write clear, concise code with descriptive names and **type hints**.
- Use concise PEP 257 docstrings for public functions/classes; keep them focused on intent.
- Add comments only when logic is non-obvious or when explaining trade-offs.
- Prefer built-in collection types for annotations (`list[str]`, `dict[str, int]`) and PEP 604 unions (`str | None`).
- Break down complex functions into smaller, focused helpers.
- Adhere to modular design, separation of concerns, and the single responsibility principle.
- Keep it simple (KISS).

## General Instructions

- Prioritize readability, clarity, and maintainability.
- Handle edge cases and implement robust error handling where needed.
- Write production-quality code with reliability, performance, and security in mind.
- Follow consistent naming conventions and language-specific best practices.
- Do not leave failing tests or type checks behind.

## Package Management

- Use `uv` and the `justfile` for workflows: `just install` (sync dev deps + install pre-commit), `uv add <package>` / `uv add --dev <package>`, `just run`, `just test`, `just check`.

## Code Style and Formatting

- Follow PEP 8 plus Ruff formatting rules from `pyproject.toml`.
- Maintain 4-space indentation per level.
- Limit lines to 120 characters.
- Place function and class docstrings immediately after the `def` or `class` line.
- Use blank lines to separate functions, classes, and logical code blocks.

## Testing and Edge Cases

- Write `pytest` tests for new functionality when appropriate.
- Test critical paths and edge cases, including empty inputs, invalid types, and large datasets.
- Keep tests focused and deterministic.

## Verification

- Run the test suite with `just test`.
- Run all pre-commit hooks with `just check`.
