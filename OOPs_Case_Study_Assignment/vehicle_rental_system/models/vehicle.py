from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class for all rentable vehicles."""

    def __init__(
        self,
        vehicle_id: str,
        registration_number: str,
        brand: str,
        model: str,
        daily_rate: float,
    ):
        if not vehicle_id.strip():
            raise ValueError("Vehicle ID cannot be empty.")
        if not registration_number.strip():
            raise ValueError("Registration number cannot be empty.")
        if not brand.strip():
            raise ValueError("Brand cannot be empty.")
        if not model.strip():
            raise ValueError("Model cannot be empty.")
        if daily_rate <= 0:
            raise ValueError("Daily rental rate must be greater than zero.")

        self._vehicle_id = vehicle_id
        self._registration_number = registration_number
        self._brand = brand
        self._model = model
        self._daily_rate = float(daily_rate)
        self._available = True

    @abstractmethod
    def calculate_rental_cost(self, days: int) -> float:
        """Return the vehicle-specific rental cost."""
        raise NotImplementedError

    def display_details(self) -> None:
        status = "Available" if self._available else "Unavailable"
        print(
            f"{self._vehicle_id} | {self.__class__.__name__} | "
            f"{self._brand} | {self._model} | "
            f"Rs. {self._daily_rate:,.0f} per day | {status}"
        )

    def mark_as_rented(self) -> None:
        self._available = False

    def mark_as_available(self) -> None:
        self._available = True

    @property
    def vehicle_id(self) -> str:
        return self._vehicle_id

    @property
    def registration_number(self) -> str:
        return self._registration_number

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def daily_rate(self) -> float:
        return self._daily_rate

    @property
    def available(self) -> bool:
        return self._available
