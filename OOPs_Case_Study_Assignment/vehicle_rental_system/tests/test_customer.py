import unittest

from models.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_required_fields(self):
        with self.assertRaises(ValueError):
            Customer("C001", "", "a@example.com", "DL001")

    def test_rental_history_is_read_only_view(self):
        customer = Customer("C001", "Test User", "a@example.com", "DL001")
        self.assertEqual(customer.rental_history, ())


if __name__ == "__main__":
    unittest.main()
