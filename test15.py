import unittest

import padlib

solve = padlib.strip_pad
exc = padlib.InvalidPadding


class Test(unittest.TestCase):
    def test_strip_pad(self):
        self.assertEqual(solve("ICE ICE BABY\x04\x04\x04\x04"), "ICE ICE BABY")
        self.assertRaises(exc, solve, "ICE ICE BABY\x05\x05\x05\x05")
        self.assertRaises(exc, solve, "ICE ICE BABY\x01\x02\x03\x04")
