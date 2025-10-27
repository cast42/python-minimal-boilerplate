"""Application entry point."""

from __future__ import annotations

import os
import sys

import logfire

GREETING: str = "Hello from python-minimal-boilerplate!"
_TOKEN: str | None = os.getenv("LOGFIRE")

# Configure Logfire once so that structured logs go to the console by default.
logfire.configure(
    token=_TOKEN,
    service_name="python-minimal-boilerplate",
    send_to_logfire=bool(_TOKEN),
    console=logfire.ConsoleOptions(output=sys.stdout),
)


def main() -> None:
    """Emit a greeting via Logfire and stdout."""
    logfire.info("application.startup", message=GREETING)
    print(GREETING)


if __name__ == "__main__":
    main()
