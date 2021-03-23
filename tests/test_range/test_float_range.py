import pytest

from assistypes.range import FloatRange


def test_incorrect_count_init_params():
    with pytest.raises(ValueError):
        FloatRange()
        FloatRange(1, 2, 3, 4)


def test_incorrect_init_params():
    with pytest.raises(ValueError):
        FloatRange(1, 10, -1)
        FloatRange(10, 1, 1)


def test_correct_step():
    i = 1.5
    result = 1

    for f in FloatRange(1, 10, 1.5):
        assert f == result
        result += i
