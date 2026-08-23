import unittest

from models.car import Car
from models.bike import Bike
from models.van import Van
from models.vehicle import Vehicle


class TestVehicles(unittest.TestCase):

    def setUp(self):
        self.car = Car("V101", "BR01AA1111", "Toyota", "Innova", 2000)
        self.bike = Bike("V102", "BR01BB2222", "Yamaha", "FZ", 700)
        self.van = Van("V103", "BR01CC3333", "Tata", "Winger", 3000, 500)

    def test_vehicle_is_abstract(self):
        with self.assertRaises(TypeError):
            Vehicle("V999", "REG999", "X", "Y", 1000)

    def test_car_cost(self):
        self.assertEqual(self.car.calculate_rental_cost(3), 6000)

    def test_bike_discount_after_five_days(self):
        self.assertEqual(self.bike.calculate_rental_cost(6), 3990)

    def test_van_service_charge(self):
        self.assertEqual(self.van.calculate_rental_cost(3), 9500)

    def test_vehicle_availability(self):
        self.assertTrue(self.car.available)
        self.car.mark_as_rented()
        self.assertFalse(self.car.available)
        self.car.mark_as_available()
        self.assertTrue(self.car.available)

    def test_invalid_registration(self):
        with self.assertRaises(ValueError):
            Car("V999", "", "Toyota", "Innova", 2000)

    def test_invalid_rate(self):
        with self.assertRaises(ValueError):
            Car("V999", "REG", "Toyota", "Innova", 0)


if __name__ == "__main__":
    unittest.main()
