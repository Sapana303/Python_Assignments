from uuid import uuid4

from .payment_processor import PaymentProcessor
from .payment_result import PaymentResult
from exceptions.rental_exceptions import PaymentFailedError


class CardPayment(PaymentProcessor):
    """Card payment implementation."""

    def __init__(self, transaction_id=None, should_succeed=True):
        self._transaction_id = transaction_id
        self._should_succeed = should_succeed

    def process_payment(self, amount):
        if amount <= 0:
            raise PaymentFailedError("Payment amount must be greater than zero.")

        if not self._should_succeed:
            raise PaymentFailedError("Card payment failed.")

        transaction_id = self._transaction_id or f"CARD-{uuid4().hex[:8].upper()}"
        return PaymentResult(transaction_id, amount, "Card")

    @property
    def transaction_id(self):
        return self._transaction_id
