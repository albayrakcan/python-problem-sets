import pytest

from datetime import date

from seasons import print_delta_minutes
from seasons import get_birthday_date


# test_get_birthday_date
def test_invalid_date(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "January 1, 1999")
    with pytest.raises(SystemExit) as exception:
        get_birthday_date()
    assert str(exception.value) == "Invalid Date"


def test_valid_date(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1999-01-01")
    result = get_birthday_date()
    expected = date(1999, 1, 1)
    assert result == expected


# test_print_delta_minutes
def test_print_delta_minutes1(capsys):
    print_delta_minutes(date.today(), date(1999, 1, 1))
    captured = capsys.readouterr()
    assert captured.out.strip() == "Fourteen million, ninety-nine thousand forty minutes"


def test_print_delta_minutes2(capsys):
    print_delta_minutes(date.today(), date(1999, 12, 31))
    captured = capsys.readouterr()
    assert (
        captured.out.strip()
        == "Thirteen million, five hundred seventy-four thousand, eight hundred eighty minutes"
    )


def test_print_delta_minutes3(capsys):
    print_delta_minutes(date.today(), date(1970, 1, 1))
    captured = capsys.readouterr()
    assert (
        captured.out.strip()
        == "Twenty-nine million, three hundred fifty-one thousand, five hundred twenty minutes"
    )


def test_print_delta_minutes_one_year(capsys):
    print_delta_minutes(date.today(), date(2024, 10, 22))
    captured = capsys.readouterr()
    assert (
        captured.out.strip() == "Five hundred twenty-five thousand, six hundred minutes"
    )


def test_print_delta_minutes_two_years(capsys):
    print_delta_minutes(date.today(), date(2023, 10, 22))
    captured = capsys.readouterr()
    assert (
        captured.out.strip()
        == "One million, fifty-two thousand, six hundred forty minutes"
    )
