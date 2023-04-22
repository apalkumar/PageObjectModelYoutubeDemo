import pytest


# with pytest framework, either all test should start with word test or ends with test
# and all the files under this framework also should start with test or ends with test

def test_m4():
    assert False


def test_m5():
    assert 100 == 100


def test_m6():
    assert "naveen" == "Naveen"


def test_login():
    assert "admin" == "admin"
