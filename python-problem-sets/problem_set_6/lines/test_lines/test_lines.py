import pytest
import sys

from lines import get_input
from lines import count_lines

# test_get_input
def test_too_few_arguments(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py"])
    with pytest.raises(SystemExit) as exc:
        get_input()
    assert str(exc.value) == "Too few command-line arguments"

def test_too_many_arguments(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py", "hello.py", "goodbye.py"])
    with pytest.raises(SystemExit) as exc:
        get_input()
    assert str(exc.value) == "Too many command-line arguments"

def test_non_python_scripts(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py", "invalid_extension.txt"])
    with pytest.raises(SystemExit) as exc:
        get_input()
    assert str(exc.value) == "Not a Python file"


# test_count_lines
def test_non_existent_file():
    with pytest.raises(SystemExit) as exc:
        count_lines("non_existent_file.py")
    assert str(exc.value) == "File does not exist"

def test_empty_script():
    assert count_lines("goodbye.py") == 0

def test_script_with_blank_lines():
    assert count_lines("hello.py") == 7

def test_script_with_comments():
    assert count_lines("average0.py") == 2

def test_script_with_docstring():
    assert count_lines("generate.py") == 15