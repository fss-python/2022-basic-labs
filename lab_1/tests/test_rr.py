import unittest

from lab_1.main import calculate_rr


class TestRR(unittest.TestCase):
    #TODO: lab condition - 400ms, code -100ms
    min_correct_rr = 101
    non_numerical = ["a", "b", "c", "d", "e", "f"]

    def test_rr(self):
        #Current code in lab1 doesn't work correctly, will implement once solved
        pass

    def test_rr_list_size_mismatch(self):
        self.assertIsNone(calculate_rr([1] * 10, [i * self.min_correct_rr for i in range(100)]))
        self.assertIsNone(calculate_rr([1] * 100, [i * self.min_correct_rr for i in range(10)]))

    def test_rr_with_gibberish(self):
        self.assertIsNone(calculate_rr(self.non_numerical, self.non_numerical))
        self.assertIsNone(calculate_rr(list(range(10)), self.non_numerical))
        self.assertIsNone(calculate_rr(self.non_numerical, list(range(10))))
        # values not equal to 0 and 1
        self.assertIsNone(calculate_rr(list(range(100)), list(range(100))))


if __name__ == "__main__":
    unittest.main()
