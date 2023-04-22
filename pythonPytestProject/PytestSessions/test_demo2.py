import pytest


# with pytest framework, either all test should start with word test or ends with test
# and all the files under this framework also should start with test or ends with test

def test_m1():
    a = 3
    b = 4
    assert a + 1 == b, "test failed"
    assert a == b, "test failed as a is not eq to b"


def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"


def test_m3():
    assert True


def test_login():
    assert "admin" == "admin"
