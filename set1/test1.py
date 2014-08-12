import base64
import binascii
import unittest


def decode_hex(string):
    return base64.b16decode(string, casefold=True)


def encode_base64(string):
    return base64.standard_b64encode(string)


def solve(string):
    return encode_base64(decode_hex(string))


class Test(unittest.TestCase):
    def test_solve(self):
        test_in = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        test_out = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEquals(solve(test_in), test_out)
