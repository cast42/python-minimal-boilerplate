# Python Coding Conventions

## Python Instructions

- Write clear and concise comments for each function.
- Ensure functions have descriptive names and include **type hints**.
- Provide **docstrings** following PEP 257 conventions, using the **Google style**:

```python
import math

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given the radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle, calculated as π * radius^2.
    """
    return math.pi ** 2
```

- Break down complex functions into smaller, manageable functions.
- Use the `typing` module for type annotations (e.g., `List[str]`, `Dict[str, int]`).
- Adhere to **modular design**, separation of concerns, and the **single responsibility principle**.
- Keep it simple: KISS (Keep It Simple, Stupid).

## General Instructions

- Always prioritize readability, clarity, and maintainability.
- Include explanations of algorithms and design decisions in comments.
- Handle **edge cases** and implement robust exception handling.
- Write code for **production environments**, focusing on reliability, performance, and security.
- Mention libraries or external dependencies with comments explaining their purpose.
- Follow consistent naming conventions and language-specific best practices.
- **Partial success is not acceptable**: aim for 100% passing tests; do not accept “almost done” results.

## Package Management

- Use **uv** for package management and virtual environments:

```bash
uv run main.py
uv run pytest
uv add <package>
```

## Code Style and Formatting

- Follow **PEP 8** style guidelines.
- Maintain **4-space indentation** per level.
- Limit lines to **79 characters**.
- Place function and class docstrings immediately after the `def` or `class` keyword.
- Use blank lines to separate functions, classes, and logical code blocks.
- Adhere to **ruff style, linting, and formatting** as defined in `pyproject.toml`.

## Testing and Edge Cases

- Write **unit tests** for all new functionality using `pytest` and `pytest-asyncio`.
- Test **critical paths and edge cases**, including empty inputs, invalid types, and large datasets.
- Document tests with docstrings explaining what is being tested and why.
- Ensure **100% test coverage**; partial success is unacceptable.

## Is your generated code correct?
- Verify by running tests: `uv run --env-file=.env python -m pytest -v tests/`
- Verify by running all pre-commit hooks if there are any: `just precommit`
