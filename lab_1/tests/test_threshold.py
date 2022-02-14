import unittest

from lab_1.main import calculate_threshold


class ThresholdTest(unittest.TestCase):
    def test_1(self):
        self.assertIsNone(calculate_threshold([1,2,3]))
