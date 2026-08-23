from .vehicle import Vehicle


class Van(Vehicle):
    """Van rental with a configurable service charge."""

    def __init__(
        self,
        vehicle_id: str,
        registration_number: str,
        brand: str,
        model: str,
        daily_rate: float,
        service_charge: float = 500.0,
    ):
        super().__init__(
            vehicle_id,
            registration_number,
            brand,
            model,
            daily_rate,
        )
        if service_charge < 0:
            raise ValueError("Service charge cannot be negative.")
        self._service_charge = float(service_charge)

    def calculate_rental_cost(self, days: int) -> float:
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")
        return self.daily_rate * days + self._service_charge

    def display_details(self) -> None:
        print(
            f"{self.vehicle_id} | Van | {self.brand} | {self.model} | "
            f"Rs. {self.daily_rate:,.0f} per day | "
            f"Service charge: Rs. {self._service_charge:,.0f} | "
            f"{'Available' if self.available else 'Unavailable'}"
        )

    @property
    def service_charge(self) -> float:
        return self._service_charge
