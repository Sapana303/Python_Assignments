class RentalError(Exception):
    """Base exception for the rental system."""


class InvalidRentalDaysError(RentalError):
    """Raised when rental duration is invalid."""


class VehicleUnavailableError(RentalError):
    """Raised when a requested vehicle cannot be rented."""


class PaymentFailedError(RentalError):
    """Raised when payment processing fails."""


class CustomerNotFoundError(RentalError):
    """Raised when a customer does not exist."""


class RentalNotFoundError(RentalError):
    """Raised when a rental record does not exist."""
