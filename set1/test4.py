import unittest

import test3


def solve():
    with open("data4.txt", "r") as f:
        best_score, the_decoder, best_msg = 0, None, None
        for msg in f:
            dec_msg, decoder, score = test3.solve(msg.rstrip())
            if score > best_score:
                best_score, the_decoder, best_msg = score, decoder, dec_msg
    return best_score, the_decoder, best_msg


class Test(unittest.TestCase):
    def test_solve(self):
        test_out = b'Now that the party is jumping\n'
        self.assertEqual(solve()[2], test_out)
