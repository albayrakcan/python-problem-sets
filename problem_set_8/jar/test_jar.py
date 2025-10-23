import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_init_2():
    jar = Jar(2)
    assert jar.capacity == 2


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    dcookie = 3
    jar = Jar()
    jar.deposit(dcookie)
    assert jar.size == dcookie
    with pytest.raises(ValueError):
        jar.deposit(12)


def test_withdraw():
    dcookie = 3
    wcookie = 2
    jar = Jar()
    jar.deposit(dcookie)
    jar.withdraw(wcookie)
    assert jar.size == dcookie - wcookie
    with pytest.raises(ValueError):
        jar.withdraw(12)
