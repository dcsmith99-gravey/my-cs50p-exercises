import pytest
from bank import value

def test_value():
    assert value("hello") == 0
    assert value("Hello, Sir") == 0

def test_zero():
    assert value("Hi") == 20

def test_hundred():
    assert value("Bye") == 100
