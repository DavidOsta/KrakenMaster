import unittest
from ..token import Token
from datetime import datetime


class TokenTest(unittest.TestCase):
    def test_price_of_a_new_token_class_is_None(self):
        token = Token("REP")
        self.assertIsNone(token.price)

    def test_stock_update_price(self):
        price = 0.215
        rep = Token("REP")
        rep.update(datetime.now(), price)
        self.assertEqual(price, rep.price)
