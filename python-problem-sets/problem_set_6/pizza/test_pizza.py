import pytest
import sys

from pizza import get_input
from pizza import tabulate_menu

# test_get_input
def test_no_argument(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["pizza.py"])
    with pytest.raises(SystemExit) as exception:
        get_input()
    assert str(exception.value) == "Too few command-line arguments"

def test_too_arguments(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["pizza.py", "regular.csv", "sicilian.csv"])
    with pytest.raises(SystemExit) as exception:
        get_input()
    assert str(exception.value) == "Too many command-line arguments"

def test_not_a_csv_file(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["pizza.py", "sicilian.txt"])
    with pytest.raises(SystemExit) as exception:
        get_input()
    assert str(exception.value) == "Not a CSV file"


# test_tabulate_menu
def test_no_csv_file():
    with pytest.raises(SystemExit) as exception:
        tabulate_menu("invalid_file.csv")
    assert str(exception.value) == "File does not exist"