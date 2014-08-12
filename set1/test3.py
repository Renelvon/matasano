import string
import unittest

import stringlib


def solve(crypt_msg):
    msg_len = len(crypt_msg) // 2  # compensate for hex encoding
    max_score, decoder = 0, 'a'
    for c in string.ascii_letters:
        xor_msg = stringlib.encode_hex(c * msg_len)
        hex_msg = stringlib.xor_hexes(crypt_msg, xor_msg)
        dec_msg = stringlib.decode_hex(hex_msg)
        score = stringlib.score(dec_msg)
        if score > max_score:
            max_score, decoder = score, c

    xor_msg = stringlib.encode_hex(decoder * msg_len)
    hex_msg = stringlib.xor_hexes(crypt_msg, xor_msg)
    return stringlib.decode_hex(hex_msg)


class Test(unittest.TestCase):
    def test_solve(self):
        test_in = b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        test_out = b"Cooking MC's like a pound of bacon"
        self.assertEqual(solve(test_in), test_out)
