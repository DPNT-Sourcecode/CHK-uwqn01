import pytest
from solutions.CHK.checkout_solution import checkout


def test_checkout():
    test1 = checkout("A, B, C, D")
    assert test1 == 115
