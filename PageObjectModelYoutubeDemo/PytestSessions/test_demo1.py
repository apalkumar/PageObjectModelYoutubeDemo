import pytest


@pytest.mark.landingpage
def test_m1():
    a = 3
    b = 4
    assert a + 1 == b, "test failed"
    assert a == b, "test failed as a is not eq to b"


@pytest.mark.home
def test_m2():
    name = "Selenium"
    assert name.upper() == "SELENIUM"


@pytest.mark.login
def test_m3():
    assert True


@pytest.mark.home
def test_m4():
    assert False


@pytest.mark.landingpage
def test_m5():
    assert 100 == 100


@pytest.mark.login
def test_m6():
    assert "naveen" == "NAVEEN"


@pytest.mark.login
def test_Login_FB():
    assert "admin" == "admin123"
