import unittest

import padlib


solve = padlib.pad_pkcs7


class Test(unittest.TestCase):
    def test_solve(self):
        test_in = "YELLOW SUBMARINE"
        length = 20
        test_out = "YELLOW SUBMARINE\x04\x04\x04\x04"
        self.assertEquals(solve(test_in, length), test_out)
