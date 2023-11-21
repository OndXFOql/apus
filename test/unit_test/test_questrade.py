import unittest

import questrade


class TestQuestradeToken(unittest.TestCase):
    def setUp(self):
        self.token = questrade.Token()

    def test_token_redeem_new_token(self):
        self.assertTrue(questrade.Token.redeem_new_token(), "failed to redeem new token.")

    # def test_token_redeem_new_token_failed(self):
    #     self.assertEqual(questrade.Token.redeem_new_token(), False, "failed to redeem new token.")


if __name__ == '__main__':
    unittest.main()
