from .vehicle import Vehicle


class Bike(Vehicle):
    """Bike rental with a 5% discount for rentals longer than five days."""

    def calculate_rental_cost(self, days: int) -> float:
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        total = self.daily_rate * days
        if days > 5:
            total *= 0.95
        return total

    def display_details(self) -> None:
        print(
            f"{self.vehicle_id} | Bike | {self.brand} | {self.model} | "
            f"Rs. {self.daily_rate:,.0f} per day | "
            f"{'Available' if self.available else 'Unavailable'}"
        )
