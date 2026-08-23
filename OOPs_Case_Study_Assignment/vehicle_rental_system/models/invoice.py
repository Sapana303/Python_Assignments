class Invoice:
    """Final billing document for a completed rental."""

    def __init__(self, rental):
        self._rental = rental
        self._base_amount = rental.base_amount
        self._late_fee = rental.late_fee
        self._final_amount = rental.total_amount

    def generate(self):
        return {
            "rental_id": self._rental.rental_id,
            "customer": self._rental.customer.name,
            "vehicle_id": self._rental.vehicle.vehicle_id,
            "base_amount": self._base_amount,
            "late_fee": self._late_fee,
            "final_amount": self._final_amount,
        }

    def display(self):
        print("-" * 60)
        print("FINAL INVOICE")
        print("-" * 60)
        print(f"Rental ID       : {self._rental.rental_id}")
        print(f"Customer        : {self._rental.customer.name}")
        print(f"Vehicle         : {self._rental.vehicle.vehicle_id}")
        print(f"Vehicle type    : {self._rental.vehicle.__class__.__name__}")
        print(f"Base amount     : Rs. {self._base_amount:,.2f}")
        print(f"Late fee        : Rs. {self._late_fee:,.2f}")
        print(f"Final amount    : Rs. {self._final_amount:,.2f}")
        print(f"Status          : {self._rental.status}")
        print("-" * 60)

    @property
    def base_amount(self):
        return self._base_amount

    @property
    def late_fee(self):
        return self._late_fee

    @property
    def final_amount(self):
        return self._final_amount
