import unittest
import collections

import stringlib


def solve(filename):
    with open(filename, "r") as f:
        min_cnt, msg = None, None
        for i, line in enumerate(f):
            unhex_msg = stringlib.decode_hex(line.rstrip())
            block_cnt = (len(unhex_msg) + 15) // 16
            blocks = (unhex_msg[16*k: 16*(k + 1)] for k in range(block_cnt))
            unequal_block_cnt = len(set(blocks))
            if min_cnt is None or unequal_block_cnt < min_cnt:
                min_cnt = unequal_block_cnt
                msg = line.rstrip()
        return min_cnt, msg


class Test(unittest.TestCase):
    def test_solve(self):
        test_in = "data8.txt"
        test_out = 'd880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a'
        self.assertEqual(solve(test_in)[1], test_out)
