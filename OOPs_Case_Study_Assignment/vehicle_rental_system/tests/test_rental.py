import unittest
from datetime import date, timedelta

from models.car import Car
from models.customer import Customer
from services.rental_service import RentalService
from payments.card_payment import CardPayment
from payments.upi_payment import UPIPayment
from exceptions.rental_exceptions import (
    PaymentFailedError,
    VehicleUnavailableError,
)


class TestRentalWorkflow(unittest.TestCase):

    def setUp(self):
        self.service = RentalService()
        self.car = Car("V101", "BR01AA1111", "Toyota", "Innova", 2000)
        self.customer_a = Customer(
            "C001", "Ananya", "ananya@example.com", "DL001"
        )
        self.customer_b = Customer(
            "C002", "Rahul", "rahul@example.com", "DL002"
        )
        self.service.add_vehicle(self.car)
        self.service.add_customer(self.customer_a)
        self.service.add_customer(self.customer_b)

    def test_unavailable_vehicle(self):
        rental = self.service.create_reservation("C001", "V101", 3)
        with self.assertRaises(VehicleUnavailableError):
            self.service.create_reservation("C002", "V101", 2)

        self.service.confirm_reservation(
            rental.rental_id,
            CardPayment(transaction_id="CARD-1"),
        )

    def test_invalid_days(self):
        with self.assertRaises(ValueError):
            self.service.create_reservation("C001", "V101", 0)

    def test_payment_failure_releases_vehicle(self):
        rental = self.service.create_reservation("C001", "V101", 3)

        with self.assertRaises(PaymentFailedError):
            self.service.confirm_reservation(
                rental.rental_id,
                UPIPayment(should_succeed=False),
            )

        self.assertTrue(self.car.available)

    def test_late_fee_and_invoice(self):
        start = date(2026, 8, 19)
        rental = self.service.create_reservation(
            "C001", "V101", 3, start_date=start
        )
        self.service.confirm_reservation(
            rental.rental_id,
            CardPayment(transaction_id="CARD-2"),
        )

        actual_return = start + timedelta(days=4)
        invoice = self.service.return_vehicle(
            rental.rental_id, actual_return
        )

        self.assertEqual(invoice.base_amount, 6000)
        self.assertEqual(invoice.late_fee, 400)
        self.assertEqual(invoice.final_amount, 6400)
        self.assertTrue(self.car.available)
        self.assertEqual(len(self.customer_a.rental_history), 1)


if __name__ == "__main__":
    unittest.main()
