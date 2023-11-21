import json
import unittest

import questrade


class TestQuestradeToken(unittest.TestCase):
    def setUp(self):
        self.token = questrade.Token()

    def test_token_sigleton(self):
        tk1 = questrade.Token()
        tk2 = questrade.Token()
        self.assertEqual(tk1, tk2, "failed to create sigleton.")

    def test_token_redeem_new_token(self):
        tk = questrade.Token()
        self.assertTrue(tk.redeem_new_token(), "failed to redeem new token.")

    def test_token_is_valid_token_false(self):
        tk = questrade.Token()
        self.assertFalse(tk.is_valid_token(), "failed is_valid_token.")

    def test_token_is_valid_token_true(self):
        json_string = '''{
            "access_token": "C3lTUKuNQrAAmSD/TPjuV/HI7aNrAwDp",
            "token_type": "Bearer",
            "expires_in": 300,
            "refresh_token": "aSBe7wAAdx88QTbwut0tiu3SYic3ox8F",
            "api_server": "https://api01.iq.questrade.com"
        }'''

        parsed_json = json.loads(json_string)

        tk = questrade.Token()
        questrade.Token._questrade_token = parsed_json

        self.assertEqual(questrade.Token._questrade_token["access_token"], "C3lTUKuNQrAAmSD/TPjuV/HI7aNrAwDp","access" )
        self.assertEqual(questrade.Token._questrade_token["expires_in"], 300,"access" )

        self.assertTrue(tk.is_valid_token(), "failed is_valid_token.")


if __name__ == '__main__':
    unittest.main()
