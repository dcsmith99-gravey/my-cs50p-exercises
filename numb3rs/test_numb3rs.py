import pytest
from numb3rs import validate

def test_higherThan():
    assert validate("260.1.0.10") is False
    assert validate("512.512.512.512") is False

def test_moreThan():
    assert validate("1111.22222.5555.0") is False
    assert validate("1.2.3.1000") is False

def test_negative():
    assert validate("-1.-255.0.0") is False

def test_longerThan():
    assert validate("0.1.245.35.36") is False

def test_Correct():
    assert validate("0.1.4.5") is True
    assert validate("255.255.0.0") is True
    assert validate("255.255.255.255") is True

def test_leadZero():
    assert validate("192.168.001.1") is False

def test_Char():
    assert validate("cat") is False
