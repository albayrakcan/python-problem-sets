import pytest
from response import validate


def test_1():
    assert validate("malan@harvard.edu") == "Valid"


def test_2():
    assert validate("can.aalbayrak@gmail.com") == "Valid"


def test_3():
    assert validate("malan@@@harvard.edu") == "Invalid"


def test_4():
    assert validate("can.aalbayrak@gmail..com") == "Invalid"
