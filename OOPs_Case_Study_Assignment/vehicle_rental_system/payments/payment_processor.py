from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Payment abstraction/contract used by RentalService."""

    @abstractmethod
    def process_payment(self, amount):
        """Process a payment and return a PaymentResult."""
        raise NotImplementedError
