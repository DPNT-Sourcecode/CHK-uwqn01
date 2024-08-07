import pytest
from solutions.CHK.checkout_solution import checkout


def test_checkout():
    test1 = checkout("A, B, C, D")
    assert test1 == 115

def test_checkout_empty():
    test1 = checkout("")
    assert test1 == -1
