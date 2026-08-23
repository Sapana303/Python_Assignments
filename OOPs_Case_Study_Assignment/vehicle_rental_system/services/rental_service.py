from datetime import date

from models.invoice import Invoice
from models.rental import Rental
from models.customer import Customer
from models.car import Car
from models.bike import Bike
from models.van import Van

from exceptions.rental_exceptions import (
    CustomerNotFoundError,
    PaymentFailedError,
    RentalNotFoundError,
    VehicleUnavailableError,
)


class RentalService:
    """Coordinates vehicle rental business workflows."""

    def __init__(self):
        self._vehicles = {}
        self._customers = {}
        self._rentals = {}
        self._next_rental_number = 1
        #self._load_default_customers() ## to check default customers
        #self._load_default_vehicles()  ## default vehicles

    def _load_default_customers(self):
        customers = [
            Customer(
                "CU001",
                "Santa",
                "santa@yahoo.com",
                "SANTA001"
            ),
            Customer(
                "CU002",
                "Raj",
                "raj@yahoo.com",
                "RAJ002"
            ),
            Customer(
                "CU003",
                "Prerna",
                "prerna@yahoo.com",
                "PRERNA003"
            )
        ]

        for customer in customers:
            self.add_customer(customer)
    
    def _load_default_vehicles(self):
        vehicles = [
            Car(
                "C001",
                "CAR001",
                "Toyota",
                "Innova",
                3000
            ),
            Bike(
                "B001",
                "BIKE001",
                "Yamaha",
                "FZ",
                1000
            ),
            Van(
                "V001",
                "VAN001",
                "Tata",
                "Winger",
                3000
            )
        ]

        for vehicle in vehicles:
            self.add_vehicle(vehicle)
    
    def add_vehicle(self, vehicle):
        self._vehicles[vehicle.vehicle_id] = vehicle

    def add_customer(self, customer):
        self._customers[customer.customer_id] = customer

    def display_customers(self):
        if not self._customers:
            print("No customers have been added yet.")
            return

        print("-" * 70)

        for customer in self._customers.values():
            print(
                f"{customer.customer_id} | "
                f"{customer.name} | "
                f"{customer.email} | "
                f"Licence: {customer.licence_number}"
            )

    def get_customer(self, customer_id):
        try:
            return self._customers[customer_id]
        except KeyError as exc:
            raise CustomerNotFoundError(
                f"Customer '{customer_id}' was not found."
            ) from exc

    def get_vehicle(self, vehicle_id):
        try:
            return self._vehicles[vehicle_id]
        except KeyError as exc:
            raise VehicleUnavailableError(
                f"Vehicle '{vehicle_id}' was not found."
            ) from exc

    def display_available_vehicles(self):
        vehicles = [v for v in self._vehicles.values() if v.available]
        if not vehicles:
            print("No vehicles are currently available.")
            return

        print("Available Vehicles")
        print("-" * 60)
        for vehicle in vehicles:
            vehicle.display_details()

    def search_vehicles(
        self,
        vehicle_id=None,
        vehicle_type=None,
        min_price=None,
        max_price=None,
    ):
        """Search by ID, type, or price range using optional parameters."""
        vehicles = list(self._vehicles.values())

        if vehicle_id:
            vehicles = [
                v for v in vehicles if v.vehicle_id.lower() == vehicle_id.lower()
            ]

        if vehicle_type:
            vehicles = [
                v
                for v in vehicles
                if v.__class__.__name__.lower() == vehicle_type.lower()
            ]

        if min_price is not None:
            vehicles = [v for v in vehicles if v.daily_rate >= min_price]

        if max_price is not None:
            vehicles = [v for v in vehicles if v.daily_rate <= max_price]

        return vehicles

    def create_reservation(
        self,
        customer_id,
        vehicle_id,
        days,
        start_date=None,
    ):
        customer = self.get_customer(customer_id)
        vehicle = self.get_vehicle(vehicle_id)

        if not vehicle.available:
            raise VehicleUnavailableError(
                f"Vehicle {vehicle.vehicle_id} is currently unavailable."
            )

        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        rental_id = f"R{self._next_rental_number:03d}"
        self._next_rental_number += 1

        rental = Rental(
            rental_id,
            customer,
            vehicle,
            days,
            start_date=start_date or date.today(),
        )

        # Temporary reservation/hold: the rental is NOT confirmed yet.
        # Confirmation happens only after successful payment.
        vehicle.mark_as_rented()
        self._rentals[rental_id] = rental
        return rental

    def confirm_reservation(self, rental_id, payment_processor):
        rental = self._get_rental(rental_id)

        if rental.status != "Reserved":
            raise PaymentFailedError(
                f"Rental {rental_id} is not awaiting payment."
            )

        try:
            payment = payment_processor.process_payment(rental.base_amount)
        except Exception as exc:
            # Release the temporary vehicle hold if payment fails.
            rental.vehicle.mark_as_available()
            del self._rentals[rental_id]
            raise PaymentFailedError(str(exc)) from exc

        rental.confirm(payment)
        return payment

    def return_vehicle(self, rental_id, actual_return_date):
        rental = self._get_rental(rental_id)

        if rental.status != "Confirmed":
            raise RentalNotFoundError(
                f"Rental {rental_id} has not been confirmed."
            )

        rental.calculate_final_amount(actual_return_date)
        rental.complete_rental()

        invoice = Invoice(rental)
        rental.invoice = invoice

        rental.vehicle.mark_as_available()
        rental.customer.add_rental(rental)

        return invoice

    def _get_rental(self, rental_id):
        try:
            return self._rentals[rental_id]
        except KeyError as exc:
            raise RentalNotFoundError(
                f"Rental '{rental_id}' was not found."
            ) from exc
