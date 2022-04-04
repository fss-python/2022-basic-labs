import unittest
import pytest

from lab_2.main import calculate_nn_pnn
from lab_1.tests.test_rr import read_test_data
from lab_2.tests import test_data_path
from lab_2.tests import non_numerical
from lab_2.tests import non_positive

class TestSDSD(unittest.TestCase):

    @pytest.mark.lab2
    def test_nn_pnn_50(self):
        nn, pnn = calculate_nn_pnn(
            read_test_data(test_data_path / 'test_rrs.txt'),
            50)

        self.assertTupleEqual(
            (
                 round(nn, 2),
                 round(pnn, 2)),
            (24, 0.67)
        )

    @pytest.mark.lab2
    def test_nn_pnn_with_gibberish(self):
        self.assertIsNone(calculate_nn_pnn(non_numerical, 2), "Only numerical values should be allowed")

    @pytest.mark.lab2
    def test_nn_pnn_test_non_pos(self):
        self.assertIsNone(calculate_nn_pnn(non_positive, 20), "Probably RRs should be > 0")

    @pytest.mark.lab2
    def test_nn_pnn_neg_tshd(self):
        self.assertIsNone(calculate_nn_pnn(non_numerical, 0), "Probably threshold should be > 0")
        self.assertIsNone(calculate_nn_pnn(non_numerical, -1), "Probably threshold should be > 0")


if __name__ == "__main__":
    unittest.main()
