import unittest

from lab_1.main import calculate_threshold


class TestThreshold(unittest.TestCase):
    # p-linear - /, y = kx + b, k > 0
    positive_test_vals = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # n-linear - \, y = kx + b, k < 0
    negative_test_vals = [-0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9, -1.0]
    # piecewise linear - /\/\/\/, p,n,p,n,p
    mixed_test_vals = [-0.1, 0.2, -0.3, 0.4, -0.5, 0.6, -0.7, 0.8, -0.9, 1.0]

    thd = 0.8
    non_numerical = ["a", "b", "c", "d", "e", "f"]


    def test_threshold_positive(self):
        self.assertEqual(calculate_threshold(self.positive_test_vals), self.thd * 1.0)

    def test_threshold_negative(self):
        self.assertEqual(calculate_threshold(self.negative_test_vals), self.thd * -0.1)

    def test_threshold_mixed(self):
        self.assertEqual(calculate_threshold(self.mixed_test_vals), self.thd * 1.0)

    def test_threshold_gibberish(self):
        self.assertIsNone(calculate_threshold(self.non_numerical), None)


if __name__ == "__main__":
    unittest.main()

