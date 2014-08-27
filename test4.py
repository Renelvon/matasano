import unittest

import test3


def solve():
    with open("data4.txt", "r") as f:
        best_msg, best_score, the_decoder = None, 0, None
        for msg in f:
            dec_msg, score, decoder = test3.solve(msg.rstrip())
            if score > best_score:
                best_msg, best_score, the_decoder = dec_msg, score, decoder
    return best_msg, best_score, the_decoder


class Test(unittest.TestCase):
    def test_solve(self):
        test_out = b'Now that the party is jumping\n'
        self.assertEqual(solve()[0], test_out)
