import os
import unittest
import pytest

from lab_2.main import save_hrv_in_file
from lab_1.tests.test_rr import read_test_data


class TestSDSD(unittest.TestCase):
    test_file = 'test_file_hrv.txt'

    @pytest.mark.lab2
    def test_save_file(self):
        hrv_characteristics = {
            'RMSSD': 5,
            'SDSD': 5,
            'NN50': 5,
            'pNN50': 5,
            'NN20': 5,
            'pNN20': 5,
        }

        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        # test return value
        save_hrv_in_file(hrv_characteristics, self.test_file)

        # test file exists
        self.assertEqual(os.path.exists(self.test_file), True, "File saving didn't work")

        # test file size
        # self.assertEqual(os.path.getsize(self.test_file), 45, "Saved file size is not equal to the expected one")


if __name__ == "__main__":
    unittest.main()
