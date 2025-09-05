from um import count

def test_cap():
    assert count("uM Um") == 2
    assert count("um um UM") == 3

def test_zero():
    assert count("hummingbird") == 0

def test_multi():
    assert count("Um hello I like to hum") == 1
    assert count("Hello, um, I would like to um test the sum of sums") == 2


