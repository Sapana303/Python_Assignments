# Vehicle Rental Management System - Class Diagram

```text
                              <<abstract>>
                           ┌─────────────────┐
                           │     Vehicle     │
                           ├─────────────────┤
                           │ - _vehicle_id   │
                           │ - _registration │
                           │ - _brand        │
                           │ - _model        │
                           │ - _daily_rate   │
                           │ - _available    │
                           ├─────────────────┤
                           │ + calculate_... │
                           │ + display_...   │
                           │ + mark_as_rented│
                           │ + mark_available│
                           └────────┬────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
            ┌──────────┐      ┌──────────┐      ┌──────────┐
            │   Car    │      │   Bike   │      │   Van    │
            ├──────────┤      ├──────────┤      ├──────────┤
            │ + cost() │      │ + cost() │      │ + cost() │
            │ + detail │      │ + detail │      │ + detail │
            └──────────┘      └──────────┘      └──────────┘

┌─────────────────┐              ┌──────────────────────────┐
│    Customer     │              │          Rental           │
├─────────────────┤              ├──────────────────────────┤
│ - customer_id   │              │ - rental_id              │
│ - name          │              │ - customer               │
│ - email         │◄─────────────│ - vehicle                │
│ - licence       │ association  │ - days                   │
│ - rental_history│              │ - payment                │
├─────────────────┤              │ - invoice                │
│ + add_rental()  │              ├──────────────────────────┤
│ + history()     │              │ + calculate_final_amount │
└─────────────────┘              │ + complete_rental()      │
                                 └────────────┬─────────────┘
                                              │ composition
                               ┌──────────────┼───────────────┐
                               │              │               │
                               ▼              ▼               ▼
                            Vehicle        Payment          Invoice

                         <<abstract>>
                    ┌────────────────────┐
                    │  PaymentProcessor  │
                    ├────────────────────┤
                    │ + process_payment()│
                    └─────────┬──────────┘
                              │
                     ┌────────┴────────┐
                     ▼                 ▼
              ┌─────────────┐   ┌─────────────┐
              │ CardPayment │   │ UPIPayment  │
              └─────────────┘   └─────────────┘


                    ┌─────────────────────┐
                    │    RentalService    │
                    ├─────────────────────┤
                    │ - vehicles          │
                    │ - customers         │
                    │ - rentals           │
                    ├─────────────────────┤
                    │ + search_vehicles() │
                    │ + create_reservation│
                    │ + confirm_reservation│
                    │ + return_vehicle()  │
                    └──────────┬──────────┘
                               │
                               │ depends on abstraction
                               ▼
                       PaymentProcessor
