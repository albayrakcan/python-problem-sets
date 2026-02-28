import pytest

from bank import value

def test_single_word():
    assert value("hello") == 0

def test_single_word_uppercase():
    assert value("Hello") == 0

def test_multiple_word():
    assert value("hello, Newman") == 0

def test_multiple_word_upercase():
    assert value("Hello, Newman") == 0

def test_20_dollars():
    assert value("How you doing?") == 20

def test_100_dollars():
    assert value("What's happening?") == 100