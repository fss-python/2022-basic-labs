import unittest
from pathlib import Path

import pytest

from lab_1.main import calculate_rr


def read_test_data(filename):
    with open(filename) as f:
        return [float(x) for x in f]


class TestRR(unittest.TestCase):
    # TODO: lab condition - 400ms, code - 100ms
    min_correct_rr = 101
    non_numerical = ["a", "b", "c", "d", "e", "f"]

    @pytest.mark.lab1
    def test_rr(self):
        test_data_path = Path(__file__).parent / 'test_data'
        self.assertListEqual(
            calculate_rr(
                read_test_data(test_data_path / 'test_spikes.txt'),
                read_test_data(test_data_path / 'test_times.txt')
            ),
            read_test_data(test_data_path / 'test_rrs.txt'))

    @pytest.mark.lab1
    def test_rr_list_size_mismatch(self):
        self.assertIsNone(calculate_rr([1] * 10, [i * self.min_correct_rr for i in range(100)]))
        self.assertIsNone(calculate_rr([1] * 100, [i * self.min_correct_rr for i in range(10)]))

    @pytest.mark.lab1
    def test_rr_with_gibberish(self):
        self.assertIsNone(calculate_rr(self.non_numerical, self.non_numerical))
        self.assertIsNone(calculate_rr(list(range(10)), self.non_numerical))
        self.assertIsNone(calculate_rr(self.non_numerical, list(range(10))))
        # values not equal to 0 and 1
        self.assertIsNone(calculate_rr(list(range(100)), list(range(100))))


if __name__ == "__main__":
    unittest.main()
