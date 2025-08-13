import pytest

from plates import is_valid

def test_str():
    assert is_valid("HELLO") == True

def test_space():
    assert is_valid("HELLO, WORLD") == False

def test_long_str():
    assert is_valid("GOODBYE") == False

def test_short_str():
    assert is_valid("A") == False

def test_number():
    assert is_valid("CS50") == True

def test_first_number():
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("PI3.14") == False

def test_all_number():
    assert is_valid("33") == False

def test_number_at_end():
    assert is_valid("AAA222") == True

