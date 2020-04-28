from data_structures_and_algorithms.challenges import __version__
from data_structures_and_algorithms.challenges.array_shift.array_shift import insert_shift_array


def test_version():
    assert __version__ == '0.1.0'


def test_empty_array():
    assert insert_shift_array([], 1) == [1]


def test_even_length_array():
    assert insert_shift_array([1, 2, 3, 4], 5) == [1, 2, 5, 3, 4]


def test_odd_length_array():
    assert insert_shift_array([1, 2, 3], 4) == [1, 2, 4, 3]
