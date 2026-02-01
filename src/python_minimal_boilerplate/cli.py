"""Command-line entry points.

This module is importable as part of the installed package, so tests can
exercise packaging/import behavior (instead of importing from the repository's
`src/` directory directly).
"""

from __future__ import annotations

import logfire

GREETING: str = "Hello from python-minimal-boilerplate!"

# 'if-token-present' means nothing will be sent (and the example still works)
# when a Logfire token/environment isn't configured.
logfire.configure(send_to_logfire="if-token-present")


def main() -> None:
    """Emit a greeting via Logfire and stdout."""
    logfire.info("application.startup", message=GREETING)
    print(GREETING)
