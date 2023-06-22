from conversion import celsius_to_fahrenheit
import pytest

def test_celsius_to_farenheit():
    assert celsius_to_fahrenheit(20) == 68

def test_celcius_to_fahrenheit_invalid():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("Invalid")

def test_celcius_to_fahrenheit_none():
    assert celsius_to_fahrenheit(None) is None
