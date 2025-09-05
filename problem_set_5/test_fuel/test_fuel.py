import pytest

from fuel import convert, gauge


def test_convert_all_str():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_convert_numenator_str():
    with pytest.raises(ValueError):
        convert("cat/4")


def test_convert_denominator_str():
    with pytest.raises(ValueError):
        convert("4/dog")


def test_convert_numbers():
    assert convert("1/4") == 25


def test_convert_numenator_bigger():
    with pytest.raises(ValueError):
        convert("4/3")


def test_convert_denominator_zero():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_negative_fractions():
    with pytest.raises(ValueError):
        convert("-1/4")


def test_gauge_low():
    assert gauge(0.7) == "E"


def test_gauge_high():
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"


def test_one_percent():
    assert gauge(1) == "E"


def test_99_percent():
    assert gauge(99) == "F"
