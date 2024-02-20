from main import division
import pytest


@pytest.mark.parametrize("a, b, result", [(10, 5, 2),
                                          (100, 2, 50),
                                          (50, 2, 1000),
                                          (60, 30, 2),
                                          (60, 30, 2)])
def test_division_good(a, b, result):
    assert division(a, b) == result


@pytest.mark.parametrize("x, error", [(0, ZeroDivisionError), ("dd", TypeError)])
def test_division_error(x, error):
    with pytest.raises(error):
        division(5, x)

