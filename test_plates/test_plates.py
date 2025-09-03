import pytest
from plates import is_valid

def test_twoletters():
    assert is_valid("AB123") is True
    assert is_valid("AB") is True
    assert is_valid("A1") is False
    assert is_valid("1A") is False

def test_max():
    assert is_valid("ABCDEFG") is False
    assert is_valid("A") is False
    assert is_valid("ABCDEF") is True


def test_numbers():
    assert is_valid("AB123") is True
    assert is_valid("AB12C") is False
    assert is_valid("CS50P") is False
    assert is_valid("AB1C") is False

def test_punc():
    assert is_valid("AAA12!") is False
    assert is_valid("A123B.") is False
    assert is_valid("AB 12") is False
    assert is_valid("AB-12") is False

def test_zero():
    assert is_valid("AB012") is False
    assert is_valid("AA0") is False
    assert is_valid("HELLO0") is False
    assert is_valid("AB100") is True



