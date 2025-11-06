"""
1. Any pytest file should start with test_ or end with _test
2. pytest method names should start with test_
3. Any code should be wrapped in method only
4. Method names should be meaningful
5. -k -> method names execution
6. -s -> logs in the output
7. -v -> more metadata
8. -m -> mark (selected test cases, @pytest.mark.)(tagging)



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
