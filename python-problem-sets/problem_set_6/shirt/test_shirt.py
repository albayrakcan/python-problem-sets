import pytest
import sys
from shirt import get_input
from shirt import check_input
from shirt import shirt


# test_get_input
def test_no_argument(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["shirt.py"])
    with pytest.raises(SystemExit) as exception:
        get_input()
    assert str(exception.value) == "Too few command-line arguments"

def test_one_argument(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["shirt.py", "before1.jpg"])
    with pytest.raises(SystemExit) as exception:
        get_input()
    assert str(exception.value) == "Too few command-line arguments"

def test_three_arguments(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["shirt.py", "before1.jpg", "before2.jpg", "before3.jpg"])
    with pytest.raises(SystemExit) as exception:
        get_input()
    assert str(exception.value) == "Too many command-line arguments"


# test_check_input()
def test_invalid_argument():
    with pytest.raises(SystemExit) as exception:
        check_input("before1.jpg", "invalid_format.bmp")
    assert str(exception.value) == "Invalid output"

def test_different_extensions():
    with pytest.raises(SystemExit) as exception:
        check_input("before1.jpg", "after1.png")
    assert str(exception.value) == "Input and output have different extensions"


# test_shirt()
def test_non_input():
    with pytest.raises(SystemExit) as exception:
        shirt("non_existent_image.jpg", "after1.jpg")
    assert str(exception.value) == "Input does not exist"
