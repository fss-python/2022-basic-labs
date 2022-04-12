import unittest

import pytest


class StubTest(unittest.TestCase):
    """
    Checks folder volume is appropriate
    """

    @pytest.mark.lab2
    def test_stub(self):
        self.assertTrue(True, msg="Test designed to succeed")
