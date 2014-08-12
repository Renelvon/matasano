import string
import unittest

import stringlib


def solve(plaintext, key):
    plainbytes = stringlib.encode_hex(bytes(plaintext, encoding='ascii'))
    ltext, lkey = len(plaintext), len(key)
    reps = (ltext + lkey - 1) // lkey
    rep_key = key * reps
    keybytes = stringlib.encode_hex(bytes(rep_key, encoding='ascii'))
    return stringlib.xor_hexes(plainbytes, keybytes)


class Test(unittest.TestCase):
    def test_solve(self):
        key = "ICE"
        plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
        ciphertext = b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
        self.assertEqual(solve(plaintext, key), ciphertext)
