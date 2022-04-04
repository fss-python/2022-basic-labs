import unittest
import pytest

from lab_1.main import detect_maximums


class TestMaximums(unittest.TestCase):
    # /\
    narrow_spike = \
        [0.1, 0.2, 0.3, 0.15, 0.07]
    narrow_spike_result = \
        [0, 0, 1, 0, 0]

    # /¯\
    flat_spike = \
        [0.1, 0.2, 0.2, 0.3, 0.3, 0.3, 0.2, 0.1]
    flat_spike_result = \
        [0, 0, 0, 0, 0, 1, 0, 0]

    # /¯\/¯\
    spike_with_local_min = \
        [0.1, 0.2, 0.2, 0.15, 0.2, 0.2, 0.1]
    spike_with_local_min_result = \
        [0, 0, 1, 0, 0, 1, 0]

    non_numerical = ["a", "b", "c", "d", "e", "f"]

    @pytest.mark.lab1
    def test_narrow_spike(self):
        self.assertListEqual(detect_maximums(self.narrow_spike, 0), self.narrow_spike_result)

    @pytest.mark.lab1
    def test_narrow_spike2(self):
        self.assertListEqual(detect_maximums(self.flat_spike, 0), self.flat_spike_result)

    @pytest.mark.lab1
    def test_spike_with_local_min(self):
        self.assertListEqual(detect_maximums(self.spike_with_local_min, 0), self.spike_with_local_min_result)

    @pytest.mark.lab1
    def test_maximums_with_gibberish(self):
        self.assertIsNone(detect_maximums(self.non_numerical, 0), None)


if __name__ == "__main__":
    unittest.main()
