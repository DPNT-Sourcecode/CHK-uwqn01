import pytest
from solutions.CHK.checkout_solution import checkout


def test_checkout():
    basket = checkout("A, B, C, D")
    assert basket == 115

def test_checkout_empty():
    basket = checkout("")
    assert basket == -1

def test_checkout_invalid():
    basket = checkout("A, B, C, E")
    assert basket == -1

def test_special_offer_checkout():
    basket = checkout("A, A, A, B, C, D")
    assert basket == 195
