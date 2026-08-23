from datetime import date, timedelta


class Rental:
    """Rental record containing customer, vehicle, payment and invoice state."""

    def __init__(self, rental_id, customer, vehicle, days, start_date=None):
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        self._rental_id = rental_id
        self._customer = customer
        self._vehicle = vehicle
        self._days = days
        self._start_date = start_date or date.today()
        self._scheduled_return_date = self._start_date + timedelta(days=days)
        self._actual_return_date = None
        self._base_amount = vehicle.calculate_rental_cost(days)
        self._late_fee = 0.0
        self._total_amount = self._base_amount
        self._status = "Reserved"
        self._payment = None
        self._invoice = None

    def calculate_final_amount(self, actual_return_date):
        if actual_return_date < self._start_date:
            raise ValueError("Return date cannot be before rental start date.")

        self._actual_return_date = actual_return_date
        late_days = max(
            0, (actual_return_date - self._scheduled_return_date).days
        )

        self._late_fee = (
            late_days * 0.20 * self._vehicle.daily_rate
        )
        self._total_amount = self._base_amount + self._late_fee
        return self._total_amount

    def complete_rental(self):
        self._status = "Completed"

    def confirm(self, payment):
        self._payment = payment
        self._status = "Confirmed"

    @property
    def rental_id(self):
        return self._rental_id

    @property
    def customer(self):
        return self._customer

    @property
    def vehicle(self):
        return self._vehicle

    @property
    def days(self):
        return self._days

    @property
    def start_date(self):
        return self._start_date

    @property
    def scheduled_return_date(self):
        return self._scheduled_return_date

    @property
    def actual_return_date(self):
        return self._actual_return_date

    @property
    def base_amount(self):
        return self._base_amount

    @property
    def late_fee(self):
        return self._late_fee

    @property
    def total_amount(self):
        return self._total_amount

    @property
    def status(self):
        return self._status

    @property
    def payment(self):
        return self._payment

    @property
    def invoice(self):
        return self._invoice

    @invoice.setter
    def invoice(self, value):
        self._invoice = value
