# Vehicle Rental Management System

A console-based Python OOP vehicle rental management system implementing a complete rental workflow for cars, bikes, and vans.

The project demonstrates core Object-Oriented Programming concepts including abstraction, inheritance, polymorphism, encapsulation, composition, association, dependency inversion, exception handling, and unit testing.

---

## Assignment Coverage

The implementation covers the following requirements:

- Abstract `Vehicle` base class
- `Car`, `Bike`, and `Van` hierarchical inheritance
- Method overriding and runtime polymorphism
- Encapsulation using protected-style private state and `@property`
- `Customer`, `Rental`, `Invoice`, and payment objects
- Composition in `Rental`
- Association between `Customer` and rental history
- Payment abstraction through `PaymentProcessor`
- Card and UPI payment implementations
- Dependency inversion: `RentalService` depends on `PaymentProcessor`
- Vehicle search by ID, type, and price range using optional parameters
- Custom exception hierarchy
- Rental validation
- Vehicle availability management
- Payment-before-confirmation
- Vehicle return handling
- Late-fee calculation
- Invoice generation and display
- Automated unit tests

---

## Business Rules

The system follows these business rules:

1. Rental days must be greater than zero.
2. A customer cannot rent an unavailable vehicle.
3. The same vehicle cannot be rented by two customers at the same time.
4. Every vehicle must have a valid registration number.
5. Payment must succeed before a rental is confirmed.
6. Late fee = late days × 20% × daily rental rate.
7. A returned vehicle becomes available again.
8. Sensitive payment information is not stored.
9. A failed payment releases the temporary vehicle hold.
10. A failed payment does not create a confirmed rental.

---

## Vehicle Rules

### Car
Rental cost = daily rate × number of days

### Bike
Rental cost = daily rate × number of days
5% discount is applied when rental duration is greater than 5 days.

### Van
Rental cost = daily rate × number of days + service charge


Each vehicle type implements its own rental-cost calculation through the common Vehicle interface/abstract contract.

## Rental Lifecycle

A rental follows these states:

```text
Reserved
   ↓
Payment
   ↓
Confirmed
   ↓
Vehicle Returned
   ↓
Completed
```

---

## Reservation and Payment Flow

When a reservation is created:

```text
Customer requests vehicle
        ↓
Customer and vehicle are validated
        ↓
Vehicle availability is checked
        ↓
Rental is created as "Reserved"
        ↓
Vehicle is temporarily held
        ↓
Payment is processed
```

### If Payment Succeeds

```text
Payment successful
        ↓
Rental becomes Confirmed
```

### If Payment Fails

```text
Payment failed
        ↓
Temporary vehicle hold is released
        ↓
Rental is removed
        ↓
PaymentFailedError is raised
```

This prevents another customer from booking the vehicle during the payment process while ensuring that the rental is not confirmed until payment succeeds.

---

## Invoice Generation

The final invoice is generated when a confirmed rental is returned.

### From the Main Menu

Select:

```text
7. Return Vehicle
```

The user enters:

```text
Rental ID
Actual return date
```

The application then performs:

```text
Return Vehicle
      ↓
Calculate final rental amount
      ↓
Calculate late fee if applicable
      ↓
Complete the rental
      ↓
Create Invoice object
      ↓
Attach invoice to Rental
      ↓
Make vehicle available
      ↓
Add rental to customer's history
      ↓
Display final invoice
```

### Invoice Code Flow

The relevant flow is:

```python
invoice = service.return_vehicle(
    rental_id,
    actual_return_date
)

invoice.display()
```

Therefore, the invoice is currently displayed automatically as part of the **Return Vehicle** operation.

There is no separate **"Print Invoice"** menu option.

---

## Mandatory Demonstration

The assignment scenario is performed through the console menu.

The required demonstration consists of:

1. Add one car, one bike, and one van.
2. Register two customers.
3. Display available vehicles.
4. Customer A reserves the car for three days.
5. Customer B attempts to reserve the same car and receives an unavailable message.
6. Customer A pays successfully.
7. Customer A returns the car one day late.
8. Base amount = Rs. 6,000.
9. Late fee = `1 × 20% × Rs. 2,000 = Rs. 400`.
10. Final amount = Rs. 6,400.
11. Final invoice is displayed.
12. The returned car becomes available again.
13. Customer A's rental history is displayed.

### Important Note About the Assignment Scenario Ordering

The assignment asks for Customer B to attempt the same vehicle before Customer A's payment, while also requiring that a rental must not be confirmed before payment succeeds.

This implementation resolves that requirement using a temporary reservation/vehicle hold:

```text
Customer A creates reservation
        ↓
Rental status = Reserved
        ↓
Vehicle is temporarily held
        ↓
Customer B cannot rent the vehicle
        ↓
Customer A completes payment
        ↓
Rental status = Confirmed
```

Therefore:

- The vehicle is unavailable during the payment process.
- The rental is not confirmed until payment succeeds.
- If payment fails, the vehicle becomes available again.

---

## OOP Mapping

| OOP Concept | Evidence in Project |
|---|---|
| Abstraction | `Vehicle(ABC)` and `PaymentProcessor(ABC)` |
| Hierarchical Inheritance | `Car(Vehicle)`, `Bike(Vehicle)`, `Van(Vehicle)` |
| Polymorphism | `vehicle.calculate_rental_cost(days)` |
| Method Overriding | Vehicle-specific rental-cost and display behavior |
| Encapsulation | Protected-style `_fields` with public properties |
| Composition | `Rental` contains references/state for customer, vehicle, payment, and invoice |
| Association | `Customer` maintains rental history |
| Interface/Contract | `PaymentProcessor` abstract contract |
| Dependency Inversion | `RentalService` receives a `PaymentProcessor` |
| Exception Handling | Custom exceptions in `rental_exceptions.py` and service/payment logic |
| Flexible Search | `search_vehicles()` uses optional filtering parameters |

---

## Why Polymorphism Improves the Design

The rental service does not need separate conditions for every vehicle type.

Instead of writing:

```python
if vehicle_type == "Car":
    ...
elif vehicle_type == "Bike":
    ...
elif vehicle_type == "Van":
    ...
```

the service can simply call:

```python
vehicle.calculate_rental_cost(days)
```

Python automatically dispatches the method to the appropriate subclass.

For example:

```text
Vehicle
   │
   ├── Car  → calculate_rental_cost()
   ├── Bike → calculate_rental_cost()
   └── Van  → calculate_rental_cost()
```

This makes the system easier to extend.

If a new vehicle type such as `Truck` is added, the new class can implement the same method without requiring major changes to the existing rental workflow.

---

## Project Structure

```text
vehicle_rental_system/
│
├── main.py
├── README.md
├── class_diagram.md
├── requirements.txt
│
├── models/
│   ├── vehicle.py
│   ├── car.py
│   ├── bike.py
│   ├── van.py
│   ├── customer.py
│   ├── rental.py
│   └── invoice.py
│
├── payments/
│   ├── payment_processor.py
│   ├── card_payment.py
│   ├── upi_payment.py
│   └── payment_result.py
│
├── services/
│   └── rental_service.py
│
├── exceptions/
│   └── rental_exceptions.py
│
└── tests/
    ├── test_vehicle.py
    ├── test_customer.py
    ├── test_rental.py
    └── test_payment.py
```

---

## Steps to Run

### 1. Create a Virtual Environment

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

The application starts as a console-based menu system.

---

## Running the Tests

Run all unit tests using:

```bash
python -m unittest discover -s tests -v
```

Expected result:

```text
Ran 17 tests

OK
```

The exact number of tests may change if additional tests are added later.

---

## Testing Coverage

The test suite covers:

### Vehicle Tests

- Abstract `Vehicle` behavior
- Car rental-cost calculation
- Bike discount
- Van service charge
- Vehicle availability
- Registration-number validation
- Daily-rate validation

### Customer Tests

- Customer validation
- Rental-history management

### Rental Tests

- Invalid rental duration
- Unavailable vehicle
- Successful rental workflow
- Payment failure
- Late-fee calculation
- Invoice creation
- Vehicle availability after return
- Customer rental history

### Payment Tests

- Successful card payment
- Successful UPI payment
- Failed card payment
- Failed UPI payment

---

## Exception Handling

The project uses custom exceptions instead of relying only on generic Python exceptions.

### Exception Hierarchy

```text
RentalError
│
├── InvalidRentalDaysError
├── VehicleUnavailableError
├── PaymentFailedError
├── CustomerNotFoundError
└── RentalNotFoundError
```

### Examples

```python
raise VehicleUnavailableError(...)
raise CustomerNotFoundError(...)
raise PaymentFailedError(...)
```

This allows the application to provide meaningful error messages for different business situations.

---

## Class Diagram

The class diagram is available in:

```text
class_diagram.md
```

The class diagram documents:

- Vehicle inheritance
- Payment abstraction
- Rental relationships
- Customer rental history
- Invoice relationship
- Service-layer dependencies

---

## Design Principles Demonstrated

The project demonstrates the following design principles.

### Single Responsibility

Different classes are responsible for different concerns:

```text
Vehicle classes   → Vehicle behavior
Customer          → Customer information/history
Rental            → Rental state and calculations
Invoice           → Invoice information/display
Payment classes   → Payment processing
RentalService     → Business workflow coordination
```

### Open/Closed Principle

New vehicle types can be introduced by extending `Vehicle` and implementing the required behavior without rewriting the complete rental workflow.

### Dependency Inversion

`RentalService` does not directly depend on a specific payment method.

Instead:

```python
def confirm_reservation(self, rental_id, payment_processor):
```

allows different payment implementations to be supplied.

For example:

```text
PaymentProcessor
       │
       ├── CardPayment
       │
       └── UPIPayment
```

This makes the payment system flexible and allows new payment methods to be added without changing the main rental workflow.
