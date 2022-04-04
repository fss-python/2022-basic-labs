import unittest
import pytest

from lab_2.main import calculate_sdnn
from lab_1.tests.test_rr import read_test_data
from lab_2.tests import test_data_path
from lab_2.tests import non_numerical
from lab_2.tests import non_positive


class TestSDNN(unittest.TestCase):
    expected_sdnn = 76.14

    @pytest.mark.lab2
    def test_sdnn(self):
        self.assertEqual(
            round(
                calculate_sdnn(
                    read_test_data(test_data_path / 'test_rrs.txt')),
                2),
            self.expected_sdnn)

    @pytest.mark.lab2
    def test_sdnn_with_gibberish(self):
        self.assertIsNone(calculate_sdnn(non_numerical), "Only numerical values should be allowed")

    @pytest.mark.lab2
    def test_sdnn_test_non_pos(self):
        self.assertIsNone(calculate_sdnn(non_positive), "Probably RRs should be > 0")


if __name__ == "__main__":
    unittest.main()
