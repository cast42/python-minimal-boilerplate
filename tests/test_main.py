"""Tests for the project's CLI entry point."""

from python_minimal_boilerplate import cli


def test_main_logs_greeting(capsys, monkeypatch) -> None:
    """The entry point should log and print the greeting."""
    calls: list[tuple[str, dict[str, str]]] = []

    def fake_info(event: str, **kwargs):
        calls.append((event, kwargs))

    monkeypatch.setattr(cli.logfire, "info", fake_info)

    cli.main()
    captured = capsys.readouterr()

    std_lines = captured.out.strip().splitlines()

    assert calls == [("application.startup", {"message": cli.GREETING})]
    assert std_lines
    assert std_lines[-1] == cli.GREETING
