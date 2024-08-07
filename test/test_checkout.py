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

def test_special_offer_checkout2():
    basket = checkout("A, A, C, B, B, D")
    assert basket == 180

def test_special_offer_checkout3():
    basket = checkout("A, A, A, A")
    assert basket == 180

def test_special_offer_checkout4():
    basket = checkout("A, A, A, B, B, B")
    assert basket == 205
