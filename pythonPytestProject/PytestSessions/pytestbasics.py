import pytest

# with pytest framework, either all test should start with word test or ends with test
# and all the files under this framework also should start with test or ends with test

def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"
