import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("5/10") == 50

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"

def test_negatives():
    with pytest.raises(ValueError):
        assert convert("-1/2")
        assert convert("-2/-2")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")

def test_nonint():
    with pytest.raises(ValueError):
        assert convert("0.5/1.54")
        assert convert("man/animal")

def test_xgtry():
    with pytest.raises(ValueError):
        assert convert("10/9")



