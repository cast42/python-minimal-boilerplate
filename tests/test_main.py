"""Tests for the project's main module."""

from src import main as app_main


def test_main_logs_greeting(capsys, monkeypatch) -> None:
    """The entry point should log and print the greeting."""
    calls: list[tuple[str, dict[str, str]]] = []

    def fake_info(event: str, **kwargs):
        calls.append((event, kwargs))

    monkeypatch.setattr(app_main.logfire, "info", fake_info)

    app_main.main()
    captured = capsys.readouterr()

    std_lines = captured.out.strip().splitlines()

    assert calls == [("application.startup", {"message": app_main.GREETING})]
    assert std_lines
    assert std_lines[-1] == app_main.GREETING
