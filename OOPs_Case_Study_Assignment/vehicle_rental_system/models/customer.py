class Customer:
    """Customer account and rental-history holder."""

    def __init__(
        self,
        customer_id: str,
        name: str,
        email: str,
        licence_number: str,
    ):
        values = {
            "Customer ID": customer_id,
            "Name": name,
            "Email": email,
            "Driving-licence number": licence_number,
        }
        for field, value in values.items():
            if not value or not value.strip():
                raise ValueError(f"{field} cannot be empty.")

        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._licence_number = licence_number
        self._rental_history = []

    def add_rental(self, rental) -> None:
        self._rental_history.append(rental)
    
    def display_rental_history(self) -> None:
        print(f"Rental history for {self._name}")
        print("-" * 90)

        if not self._rental_history:
            print("No completed rentals.")
            return

        # Table header
        print(
            f"{'Rental ID':<12} | "
            f"{'Vehicle ID':<12} | "
            f"{'Vehicle Type':<15} | "
            f"{'Days':<8} | "
            f"{'Total Amount':<18} | "
            f"{'Status':<12}"
        )

        print("-" * 90)

        # Table rows
        for rental in self._rental_history:
            print(
                f"{rental.rental_id:<12} | "
                f"{rental.vehicle.vehicle_id:<12} | "
                f"{rental.vehicle.__class__.__name__:<15} | "
                f"{rental.days:<8} | "
                f"{'Rs. ' + format(rental.total_amount, ',.2f'):<18} | "
                f"{rental.status:<12}"
            )

    # def display_rental_history(self) -> None:
    #     print(f"Rental history for {self._name}")
    #     print("-" * 60)

    #     if not self._rental_history:
    #         print("No completed rentals.")
    #         return

    #     for rental in self._rental_history:
    #         print(
    #             f"{rental.rental_id} | {rental.vehicle.vehicle_id} | "
    #             f"{rental.vehicle.__class__.__name__} | "
    #             f"{rental.days} days | "
    #             f"Rs. {rental.total_amount:,.2f} | "
    #             f"{rental.status}"
    #         )

    @property
    def customer_id(self) -> str:
        return self._customer_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def licence_number(self) -> str:
        return self._licence_number

    @property
    def rental_history(self):
        return tuple(self._rental_history)
