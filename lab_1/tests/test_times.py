import unittest

import pytest

from lab_1.main import calculate_times


class TestTimes(unittest.TestCase):
    dummy_list = list(range(100))
    type(dummy_list)
    non_numerical = ["a", "b", "c", "d", "e", "f"]

    @pytest.mark.lab1
    def test_times_10Hz(self):
        self.assertListEqual(calculate_times(self.dummy_list, 10), [i * 100 for i in self.dummy_list])

    @pytest.mark.lab1
    def test_times_100Hz(self):
        self.assertListEqual(calculate_times(self.dummy_list, 100), [i * 10 for i in self.dummy_list])

    @pytest.mark.lab1
    def test_times_1KHz(self):
        self.assertListEqual(calculate_times(self.dummy_list, 1000), self.dummy_list)

    @pytest.mark.lab1
    def test_times_with_gibberish(self):
        self.assertIsNone(calculate_times(self.non_numerical, 100))


if __name__ == "__main__":
    unittest.main()
