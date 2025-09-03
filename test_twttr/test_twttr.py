import pytest
from twttr import shorten

def test_shorten():
    assert shorten("test") == "tst"
    assert shorten("aeiou") == ""
    assert shorten("TEAIOUST") == "TST"

def test_numbers():
    assert shorten("H3ll0") == "H3ll0"

def test_punctuation():
    assert shorten("Hey! Love, you.") == "Hy! Lv, y."

