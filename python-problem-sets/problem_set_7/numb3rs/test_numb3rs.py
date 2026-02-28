import pytest

from numb3rs import validate

def test_regular_ip():
    assert validate("127.0.0.1") == True

def test_maximum():
    assert validate("255.255.255.255") == True

def test_exceeds_limit():
    assert validate("512.512.512.512") == False

def test_exceeds_digit_limit():
    assert validate("1.2.3.1000") == False

def test_exceeds_dot():
    assert validate("192.168.001.1") == False

def test_string_input():
    assert validate("cat") == False
