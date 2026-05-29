# test_celsius_to_fahrenheit.py
import pytest

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_celsius_to_fahrenheit_zero():
    assert celsius_to_fahrenheit(0) == 32

def test_celsius_to_fahrenheit_hundred():
    assert celsius_to_fahrenheit(100) == 212

def test_celsius_to_fahrenheit_negative():
    assert celsius_to_fahrenheit(-40) == -40

def test_celsius_to_fahrenheit_invalid_input():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("a")

def test_celsius_to_fahrenheit_invalid_input2():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(1.2)
