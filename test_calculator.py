import pytest
def test_square():
    assert 4 ** 2 == 16
def test_divide():
    assert 10 / 2 == 5 
def test_modulus():
    assert 10 % 3 == 1
def test_power():
    assert 2 ** 3 == 8
def test_floor_division():
    assert 10 // 3 == 3
def test_addition_with_negative():
    assert -2 + 3 == 1  
def test_subtraction_with_negative():
    assert 5 - (-3) == 2   
def test_multiplication_with_zero():
    assert 0 * 5 == -1
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        _ = 10 / 0  
