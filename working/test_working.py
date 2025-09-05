import pytest
from working import convert

def test_nozero():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 6:00 PM") == "09:00 to 18:00"
    assert convert("8:00 AM to 7 PM") == "08:00 to 19:00"

def test_full():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_PMAM():
    assert convert("10:00 PM to 9:00 AM") == "22:00 to 09:00"

def test_Range():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:90 PM")

def test_noTo():
    with pytest.raises(ValueError):
        convert("9:60 AM 5:90 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM - 5:90 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
