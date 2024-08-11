import pytest
from solutions.CHK.checkout_solution import checkout


def test_checkout():
    basket = checkout("A, B, C, D")
    assert basket == 115


def test_checkout_empty():
    basket = checkout("")
    assert basket == 0


def test_checkout_invalid():
    basket = checkout("A, B, C, E")
    assert basket == 140


def test_checkout_invalid2():
    basket = checkout("A, B, C, 4")
    assert basket == -1


def test_checkout_valid():
    basket = checkout("A,B,C,D")
    assert basket == 115


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


def test_special_offer_checkout5():
    basket = checkout("A, A, A, A, A, A")
    assert basket == 250


def test_special_offer_checkout6():
    basket = checkout("A, A, A, A, A, A, A")
    assert basket == 300


def test_checkout2():
    basket = checkout("A")
    assert basket == 50


def test_checkout3():
    basket = checkout("B")
    assert basket == 30


def test_checkout4():
    basket = checkout("C")
    assert basket == 20


def test_checkout5():
    basket = checkout("D")
    assert basket == 15


def test_checkout6():
    basket = checkout("a")
    assert basket == -1


def test_checkout7():
    basket = checkout("AAAA")
    assert basket == 180


def test_checkout8():
    basket = checkout("aaaa")
    assert basket == -1

def test_checkout9():
    basket = checkout("-")
    assert basket == -1


def test_checkout10():
    assert checkout("ABCa") == -1


def test_checkout11():
    assert checkout("AxA") == -1


def test_checkout12():
    assert checkout("ABCD") == 115
    assert checkout("AA") == 100
    assert checkout("AAA") == 130
    assert checkout("AAAA") == 180
    assert checkout("AAAAA") == 200
    assert checkout("AAAAAA") == 250
    assert checkout("B") == 30
    assert checkout("BB") == 45
    assert checkout("BBB") == 75
    assert checkout("BBBB") == 90
    assert checkout("ABCDABCD") == 215
    assert checkout("BABDDCAC") == 215
    assert checkout("AAABB") == 175
    assert checkout("AAAAAAABBBBBCCCD") == (200)+(2*50)+(5*30)+(3*20)+(15)


def test_checkout13():
    assert checkout("ABCEE") == 150
    assert checkout("AECDE") == 165
    assert checkout("AECDEE") == 205
    assert checkout("ABEEEE") == 210
    assert checkout("ABBEEEE") == 220



