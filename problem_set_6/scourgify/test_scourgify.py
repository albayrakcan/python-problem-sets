import pytest
import sys
from scourgify import get_input
from scourgify import scourgify

# test_get_input()
def test_no_argument(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["scourgify.py"])
    with pytest.raises(SystemExit) as exception:
        get_input()
    assert str(exception.value) == "Too few command-line arguments"

def test_one_argument(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["scourgify.py", "1.csv"])
    with pytest.raises(SystemExit) as exception:
        get_input()
    assert str(exception.value) == "Too few command-line arguments"

def test_three_arguments(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["scourgify.py", "1.csv", "2.csv", "3.csv"])
    with pytest.raises(SystemExit) as exception:
        get_input()
    assert str(exception.value) == "Too many command-line arguments"


# test_scourgify()
def test_invalid_file():
    with pytest.raises(SystemExit) as exception:
        scourgify("invalid_file.csv", "output.csv")
    assert str(exception.value) == "Could not read invalid_file.csv"
