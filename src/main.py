"""Application entry point."""

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


if __name__ == "__main__":
    main()
