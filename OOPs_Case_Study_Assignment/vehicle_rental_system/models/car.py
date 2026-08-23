from .vehicle import Vehicle


class Car(Vehicle):
    """Car rental: daily rate multiplied by rental days."""

    def calculate_rental_cost(self, days: int) -> float:
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")
        return self.daily_rate * days

    def display_details(self) -> None:
        print(
            f"{self.vehicle_id} | Car | {self.brand} | {self.model} | "
            f"Rs. {self.daily_rate:,.0f} per day | "
            f"{'Available' if self.available else 'Unavailable'}"
        )
