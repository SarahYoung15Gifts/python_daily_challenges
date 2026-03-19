from importlib import util
from pathlib import Path

import pytest

# script to run test: python -m pytest -q test_day_15_library_system.py


# Load the target script as a module because its filename contains hyphens.
MODULE_PATH = Path(__file__).with_name("day-15_library_system.py")
SPEC = util.spec_from_file_location("day15_module", MODULE_PATH)
DAY15 = util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(DAY15)


def _set_inputs(monkeypatch, values):
    responses = iter(values)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(responses))


@pytest.mark.parametrize(
    "title",
    [
        "The Great Gatsby",
        "Book 2",
        "Hello, World!",
        "A/B Test (2026)",
    ],
)
def test_is_valid_title_accepts_valid_inputs(title):
    assert DAY15.is_valid_title(title) is True


@pytest.mark.parametrize(
    "title",
    [
        "",
        "Bad|Title",
        "Emoji title 😀",
        "Name with @ sign",
    ],
)
def test_is_valid_title_rejects_invalid_inputs(title):
    assert DAY15.is_valid_title(title) is False


@pytest.mark.parametrize("author", ["Jane Doe", "F. Scott Fitzgerald", "A B C"])
def test_is_valid_author_accepts_valid_inputs(author):
    assert DAY15.is_valid_author(author) is True


@pytest.mark.parametrize("author", ["", "John3", "Mary-Jane", "Author!"])
def test_is_valid_author_rejects_invalid_inputs(author):
    assert DAY15.is_valid_author(author) is False


def test_ask_yes_no_retries_until_valid(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["maybe", "y"])

    result = DAY15.ask_yes_no("Continue? ")

    assert result is True
    output = capsys.readouterr().out
    assert "Please enter yes or no." in output


def test_get_title_input_retries_on_invalid_then_returns_valid(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["", "Bad|Title", "Clean Title"])

    title, done = DAY15.get_title_input([])

    assert title == "Clean Title"
    assert done is False
    output = capsys.readouterr().out
    assert "Title cannot be empty." in output
    assert "Invalid title." in output


def test_get_title_input_duplicate_allows_continue(monkeypatch, capsys):
    books = [DAY15.Book("Existing", 2020, "Jane")]
    _set_inputs(monkeypatch, ["Existing", "yes"])

    title, done = DAY15.get_title_input(books)

    assert title == "Existing"
    assert done is False
    output = capsys.readouterr().out
    assert "Warning: This title is already submitted." in output


def test_get_title_input_duplicate_user_finishes(monkeypatch, capsys):
    books = [DAY15.Book("Existing", 2020, "Jane")]
    _set_inputs(monkeypatch, ["Existing", "no", "yes"])

    title, done = DAY15.get_title_input(books)

    assert title == ""
    assert done is True
    output = capsys.readouterr().out
    assert "Warning: This title is already submitted." in output


def test_get_year_input_retries_until_numeric(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["abc", "2026"])

    year = DAY15.get_year_input()

    assert year == 2026
    output = capsys.readouterr().out
    assert "Invalid year. Please enter numbers only." in output


def test_get_author_input_retries_until_valid(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["", "Jane2", "Jane Doe"])

    author = DAY15.get_author_input()

    assert author == "Jane Doe"
    output = capsys.readouterr().out
    assert "Author cannot be empty." in output
    assert "Invalid author. Use only letters, spaces, and full stops." in output


def test_main_single_entry_flow(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["Book One", "2020", "Jane Doe", "yes"])

    DAY15.main()

    output = capsys.readouterr().out
    assert "Books entered:" in output
    assert "Title: Book One, Year: 2020" in output
    assert "Author: Jane Doe" in output
