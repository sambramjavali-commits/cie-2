from largest import largest

def test_first():
    assert largest(30, 20, 10) == 30

def test_second():
    assert largest(10, 40, 20) == 40

def test_third():
    assert largest(10, 20, 50) == 50

