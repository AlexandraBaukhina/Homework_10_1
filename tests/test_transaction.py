import unittest
from unittest.mock import patch

from src.transaction import get_transaction_amount


class TestTransaction(unittest.TestCase):
    @patch("external_api.convert_currency")
    def test_get_transaction_amount(self, mock_convert_currency):
        transaction = {"amount": 100, "currency": "USD"}
        mock_convert_currency.return_value = 1.3

        result = get_transaction_amount(transaction)

        self.assertEqual(result, 1.3)


if __name__ == "__main__":
    unittest.main()
