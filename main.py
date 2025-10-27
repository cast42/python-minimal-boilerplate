import os

import logfire


def main():
    print("Hello from python-minimal-boilerplate!")


if __name__ == "__main__":
    logfire_token = os.environ.get("LOGFIRE")
    if logfire_token:
        logfire.configure(
            token=logfire_token,
            console=False,
            service_name="python-minimal-boilerplate",
        )
    else:
        logfire.configure(
            service_name="python-minimal-boilerplate",
            send_to_logfire=False,
            console=False,
        )

    logfire.info("Starting PDF to Markdown conversion tool")
    main()
