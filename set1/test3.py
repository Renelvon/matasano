import unittest

from Crypto.Util import strxor

import stringlib


def solve(crypt_msg):
    max_score, decoder, secret = 0, None, None
    unhex_msg = stringlib.decode_hex(crypt_msg)
    for c in range(256):
        dec_msg = strxor.strxor_c(unhex_msg, c)
        score = stringlib.score(dec_msg)
        if score > max_score:
            max_score, decoder, secret = score, c, dec_msg

    return secret, max_score, decoder


class Test(unittest.TestCase):
    def test_solve(self):
        test_in = b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        test_out = b"Cooking MC's like a pound of bacon"
        self.assertEqual(solve(test_in)[0], test_out)
