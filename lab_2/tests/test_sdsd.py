import unittest
import pytest

from lab_2.main import calculate_sdsd
from lab_1.tests.test_rr import read_test_data
from lab_2.tests import test_data_path
from lab_2.tests import non_numerical
from lab_2.tests import non_positive


class TestSDSD(unittest.TestCase):
    expected_sdsd = 53.75

    @pytest.mark.lab2
    def test_sdsd(self):
        self.assertEqual(
            round(
                calculate_sdsd(
                    read_test_data(test_data_path / 'test_rrs.txt')),
                2),
            self.expected_sdsd)

    @pytest.mark.lab2
    def test_sdsd_with_gibberish(self):
        self.assertIsNone(calculate_sdsd(non_numerical), "Only numerical values should be allowed")

    @pytest.mark.lab2
    def test_sdsd_test_non_pos(self):
        self.assertIsNone(calculate_sdsd(non_positive), "Probably RRs should be > 0")


if __name__ == "__main__":
    unittest.main()
