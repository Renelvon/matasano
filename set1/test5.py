import string
import unittest

from Crypto.Util import strxor

import stringlib


def solve(plaintext, key):
    ltext, lkey = len(plaintext), len(key)
    reps = (ltext + lkey - 1) // lkey
    rep_key = (key * reps)[:ltext]
    ciphertext = strxor.strxor(plaintext, rep_key)
    return stringlib.encode_hex(ciphertext).lower()


class Test(unittest.TestCase):
    def test_solve(self):
        key = b"ICE"
        plaintext = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
        ciphertext = b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
        self.assertEqual(solve(plaintext, key), ciphertext)
