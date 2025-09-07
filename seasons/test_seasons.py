import pytest
from seasons import words

def test_words():
    assert words(60) == "Sixty"
    assert words(200) == "Two hundred"
    assert words(10501) == "Ten thousand, five hundred one"
