import unittest
import pytest

from lab_2.main import calculate_rmssd
from lab_1.tests.test_rr import read_test_data
from lab_2.tests import test_data_path
from lab_2.tests import non_numerical
from lab_2.tests import non_positive


class TestRMSSD(unittest.TestCase):
    expected_rmssd = 53.01

    @pytest.mark.lab2
    def test_rmssd(self):
        self.assertEqual(
            round(
                calculate_rmssd(
                    read_test_data(test_data_path / 'test_rrs.txt')),
                2),
            self.expected_rmssd)

    @pytest.mark.lab2
    def test_rmssd_with_gibberish(self):
        self.assertIsNone(calculate_rmssd(non_numerical), "Only numerical values should be allowed")

    @pytest.mark.lab2
    def test_rmssd_test_non_pos(self):
        self.assertIsNone(calculate_rmssd(non_positive), "Probably RRs should be > 0")


if __name__ == "__main__":
    unittest.main()
