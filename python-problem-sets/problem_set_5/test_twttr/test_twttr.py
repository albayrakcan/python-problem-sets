import pytest
from twttr import shorten

def test_sigle_word():
    assert shorten("Twitter") == "Twttr"

def test_sigle_word_uppercase():
    assert shorten("TwIttEr") == "Twttr"

def test_multiple_words():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_multiple_words_uppercase():
    assert shorten("WhAt's yOUr nAmE?") == "Wht's yr nm?"

def test_int():
    assert shorten("CS50") == "CS50"