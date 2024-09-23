import unittest
from unittest.mock import Mock, patch

from src.external_api import convert_currency, get_exchange_rate


class TestExternalAPI(unittest.TestCase):
    @patch("external_api.requests.get")
    def test_get_exchange_rate(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"rates": {"USD": 0.013, "EUR": 0.011}}
        mock_get.return_value = mock_response

        exchange_rate_usd = get_exchange_rate("RUB", "USD")
        exchange_rate_eur = get_exchange_rate("RUB", "EUR")

        self.assertEqual(exchange_rate_usd, 0.013)
        self.assertEqual(exchange_rate_eur, 0.011)

    @patch("external_api.get_exchange_rate")
    def test_convert_currency(self, mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = 0.013

        converted_amount = convert_currency(100, "USD", "RUB")

        self.assertEqual(converted_amount, 1.3)
