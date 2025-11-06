"""
1. Any pytest file should start with test_ or end with _test
2. pytest method names should start with test_



"""
import pytest


@pytest.mark.smoke
def test_firstprogram():
    print("Hello")

@pytest.mark.skip
def test_secondprogram():
    print("i am second program")


def test_uiautomation():
    print("I am uiautomation from first file")