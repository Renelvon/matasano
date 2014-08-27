import unittest

import stringlib


def solve(bstring):
    dec_hex = stringlib.decode_hex(bstring)
    enc_base64 = stringlib.encode_base64(dec_hex)
    return enc_base64


class Test(unittest.TestCase):
    def test_solve(self):
        test_in = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        test_out = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEquals(solve(test_in), test_out)
