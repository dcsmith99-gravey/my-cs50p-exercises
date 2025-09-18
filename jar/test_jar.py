import pytest
from jar import Jar

def test_init():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0

    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar(2.68)
    with pytest.raises(ValueError):
        Jar("15")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    j = Jar(5)
    j.deposit(2)
    assert j.size == 2
    j.deposit(3)
    assert j.size == 5
    with pytest.raises(ValueError):
        j.deposit(1)

def test_withdraw():
    j = Jar(6)
    j.deposit(4)
    j.withdraw(1)
    assert j.size == 3
    j.withdraw(3)
    assert j.size == 0
    with pytest.raises(ValueError):
        j.withdraw(1)
