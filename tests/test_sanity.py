from pytest import approx
import numpy as np
import pytest

# Parametrize
def test_sanity_check():
    assert 2 + 2 == 4

@pytest.mark.parametrize("x,y", [(5,5),(10,10)])
def test_same_number(x,y):
    assert x == y

@pytest.mark.parametrize("x,y, expected", [(5,5,10),(10,10,20)])
def test_add_number(x,y, expected):
    assert x + y == expected

@pytest.mark.parametrize('x,y', [(3.141595674, 3.1416), (2.0, 2.0001)])
def test_float(x,y):
    assert x == approx(y, rel=1e-4)

def test_array():
    a = np.array([1,2,3])
    b = np.array([1.0,1.999567,3.000002])
    np.testing.assert_allclose(a, b, rtol=1e-1)