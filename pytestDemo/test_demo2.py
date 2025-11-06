"""
1. Any pytest file should start with test_ or end with _test
2. pytest method names should start with test_
3. Any code should be wrapped in method only
4. Method names should be meaningful
5. -k -> method names execution
6. -s -> logs in the output
7. -v -> more metadata
8. -m -> mark (selected test cases, @pytest.mark.)(tagging) and then run with -m
9. mark.xfail -> pass fail status is not recorded
10. skip tests with @pytest.mark.skip
11. fixtures are used as setup and tear down methods for test cases.
12. conftest file is used to generalise fixtures and make it available to all test cases



"""
import pytest


def test_firstprogram():
    msg = "Hello"
    assert msg == "Hi", "Test failed as Strings do not match"


def test_secondprogram():
    a = 6
    b = 5
    assert b + 2 == a,"Values do not match"

@pytest.mark.smoke
def test_uiautomation():
    print("I am uiautomation from second file")


@pytest.fixture()
def setup():
    print("I will be executed first")


def test_fixtureDemo(setup):
    print("I will execute steps in fixturedemo method")
