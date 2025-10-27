"""Tests for the project's main module."""

from main import main


def test_main_prints_greeting(capsys) -> None:
    """The entry point should print the expected greeting."""
    main()
    captured = capsys.readouterr()

    assert captured.out == "Hello from python-minimal-boilerplate!\n"
