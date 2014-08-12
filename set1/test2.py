import unittest

import stringlib


def solve(hex1, hex2):
    return stringlib.xor_hexes(hex1, hex2)

class Test(unittest.TestCase):
    def test_solve(self):
        test_in_1 = b"1c0111001f010100061a024b53535009181c" 
        test_in_2 = b"686974207468652062756c6c277320657965"
        test_out = b"746865206b696420646f6e277420706c6179"
        self.assertEquals(solve(test_in_1, test_in_2), test_out)
