import pytest

from assistypes.list import StructuredList


def test_list_behavior():
    lst = StructuredList(range(10))
    assert lst == list(range(10))

    lst.append(10)
    assert lst == list(range(11))

    lst.extend(range(11, 20))
    assert lst == list(range(20))


def test_correct_resize():
    lst = StructuredList(range(12))
    assert lst.size == (12,)

    lst.resize((2, 2, 3))
    assert lst == [
        [[0, 1, 2], [3, 4, 5]],
        [[6, 7, 8], [9, 10, 11]],
    ]


def test_correct_linearize():
    lst = StructuredList([
        [[0, 1, 2], [3, 4, 5]],
        [[6, 7, 8], [9, 10, 11]],
    ])

    assert lst.size == (2, 2, 3)

    assert lst.get_linear() == list(range(12))
