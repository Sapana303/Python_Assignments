import unittest

from payments.card_payment import CardPayment
from payments.upi_payment import UPIPayment
from exceptions.rental_exceptions import PaymentFailedError


class TestPayments(unittest.TestCase):

    def test_card_success(self):
        result = CardPayment(transaction_id="CARD-TEST").process_payment(1000)
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.method, "Card")
        self.assertEqual(result.amount, 1000)

    def test_upi_success(self):
        result = UPIPayment(transaction_id="UPI-TEST").process_payment(1000)
        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.method, "UPI")

    def test_card_failure(self):
        with self.assertRaises(PaymentFailedError):
            CardPayment(should_succeed=False).process_payment(1000)

    def test_upi_failure(self):
        with self.assertRaises(PaymentFailedError):
            UPIPayment(should_succeed=False).process_payment(1000)


if __name__ == "__main__":
    unittest.main()
