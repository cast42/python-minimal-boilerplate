"""Application entry point.

Kept as a tiny shim so `python -m src.main` continues to work for newcomers.
The actual implementation lives in the installable package.
"""

from python_minimal_boilerplate.cli import main


if __name__ == "__main__":
    main()
