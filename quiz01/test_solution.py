import pytest
from solution import convert


def test_basic_numerals():
    assert convert("I") == 1
    assert convert("V") == 5
    assert convert("X") == 10


def test_addition():
    assert convert("III") == 3
    assert convert("VIII") == 8
    assert convert("XII") == 12


def test_subtraction():
    assert convert("IV") == 4
    assert convert("IX") == 9
    assert convert("XL") == 40
    assert convert("XC") == 90
    assert convert("CD") == 400
    assert convert("CM") == 900


def test_complex_numbers():
    assert convert("XIV") == 14
    assert convert("XLII") == 42
    assert convert("MCMXCIV") == 1994