import pytest

from assistypes.range import RoundedRange


def test_incorrect_count_init_params():
    with pytest.raises(ValueError):
        RoundedRange()
        RoundedRange(1, 2, 3, 4)


def test_incorrect_init_params():
    with pytest.raises(ValueError):
        RoundedRange(1, 10, -1)
        RoundedRange(10, 1, 1)


def test_correct_step():
    i = 1.333
    result = 1

    for r in RoundedRange(1, 10, 1.333):
        assert r == result
        result += i
        result = round(result, 3)
