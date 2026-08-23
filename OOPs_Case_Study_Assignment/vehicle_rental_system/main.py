from models.car import Car
from models.bike import Bike
from models.van import Van
from models.customer import Customer
from payments.card_payment import CardPayment
from payments.upi_payment import UPIPayment
from datetime import datetime
from services.rental_service import RentalService


def show_menu():
    print("\n")
    print("=" * 55)
    print("        VEHICLE RENTAL MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Add Vehicle")
    print("2. Add Customer")
    print("3. Display All Vehicles")
    print("4. Display Available Vehicles")
    print("5. Rent Vehicle")
    print("6. Make Payment")
    print("7. Return Vehicle")
    print("8. Show Customer Rental History")
    print("9. Show All Customers")
    print("10. Exit")
    print("=" * 55)

service = RentalService()

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n========== ADD VEHICLE ==========")
        print("1. Car")
        print("2. Bike")
        print("3. Van")

        vehicle_type = input("Enter vehicle type: ")

        vehicle_id = input("Enter Vehicle ID: ")
        registration_number = input("Enter Registration Number: ")
        make = input("Enter Maker: ")
        model = input("Enter Model: ")
        daily_rate = float(input("Enter Daily Rental Rate: "))

        if vehicle_type == "1":
            vehicle = Car(
            vehicle_id,
            registration_number,
            make,
            model,
            daily_rate
        )

        elif vehicle_type == "2":
            vehicle = Bike(
            vehicle_id,
            registration_number,
            make,
            model,
            daily_rate
        )

        elif vehicle_type == "3":
            vehicle = Van(
            vehicle_id,
            registration_number,
            make,
            model,
            daily_rate
        )

        else:
            print("Invalid vehicle type.")
            continue

        service.add_vehicle(vehicle)

        print("\nVehicle added successfully!")

  
    
    elif choice == "2":
        print("\n========== ADD CUSTOMER ==========")
        customer_id = input("Enter Customer ID: ")
        name = input("Enter Customer Name: ")
        email = input("Enter Email: ")
        licence_number = input("Enter Driving Licence Number: ")

        try:
            customer = Customer(
            customer_id,
            name,
            email,
            licence_number
            )

            service.add_customer(customer)

            print("\nCustomer added successfully!")

        except ValueError as e:
            print(f"\nError: {e}")
            

    elif choice == "3":
        print("\n========== ALL VEHICLES ==========")
        vehicles = service.search_vehicles()
        if not vehicles:
            print("No vehicles have been added yet.")
        else:
            print("-" * 70)

        for vehicle in vehicles:
            vehicle.display_details()

    elif choice == "4":
        print()
        service.display_available_vehicles()

    elif choice == "5":
        print("\n========== RENT VEHICLE ==========")
        customer_id = input("Enter Customer ID: ")
        vehicle_id = input("Enter Vehicle ID: ")

        try:
            days = int(input("Enter Number of Days: "))
            rental = service.create_reservation(
                customer_id,
                vehicle_id,
                days
            )
            print("\n========== RENTAL CREATED ==========")
            print(f"Rental ID          : {rental.rental_id}")
            print(f"Customer           : {rental.customer.name}")
            print(f"Vehicle ID         : {rental.vehicle.vehicle_id}")
            print(f"Vehicle Type       : {rental.vehicle.__class__.__name__}")
            print(f"Rental Days        : {rental.days}")
            print(f"Start Date         : {rental.start_date}")
            print(f"Scheduled Return   : {rental.scheduled_return_date}")
            print(f"Base Amount        : Rs. {rental.base_amount:,.2f}")
            print(f"Status             : {rental.status}")
            print("\nPayment is required to confirm the rental.")

        except Exception as e:
            print(f"\nError: {e}")
    
    elif choice == "6":
        print("\n========== MAKE PAYMENT ==========")
        rental_id = input("Enter Rental ID: ")
        print("\nSelect Payment Method:")
        print("1. Card")
        print("2. UPI")

        payment_choice = input("Enter your choice: ")

        if payment_choice == "1":
            payment_processor = CardPayment()

        elif payment_choice == "2":
            payment_processor = UPIPayment()
            
        else:
            print("\nInvalid payment method.")
            continue

        try:
            payment = service.confirm_reservation(
                rental_id,
                payment_processor
            )

            print("\n========== PAYMENT SUCCESSFUL ==========")
            print(f"Transaction ID : {payment.transaction_id}")
            print(f"Amount         : Rs. {payment.amount:,.2f}")
            print(f"Payment Method : {payment.method}")
            print(f"Status         : {payment.status}")

            print("\nRental confirmed successfully.")

        except Exception as e:
            print(f"\nPayment Error: {e}")

    elif choice == "7":
        print("\n========== RETURN VEHICLE ==========")

        rental_id = input("Enter Rental ID: ")
        return_date_input = input(
            "Enter Actual Return Date (YYYY-MM-DD): "
        )

        try:
            actual_return_date = datetime.strptime(
                return_date_input,
                "%Y-%m-%d"
            ).date()

            invoice = service.return_vehicle(
                rental_id,
                actual_return_date
            )

            print("\n========== VEHICLE RETURNED ==========")

            invoice.display()

            print("\nVehicle returned successfully.")

        except ValueError as e:
            print(f"\nError: {e}")
            
        except Exception as e:
            print(f"\nError: {e}")

    elif choice == "8":
        print("\n========== CUSTOMER RENTAL HISTORY ==========")

        customer_id = input("Enter Customer ID: ")

        try:
            customer = service.get_customer(customer_id)
            customer.display_rental_history()

        except Exception as e:
            print(f"\nError: {e}")
    
    elif choice == "9":
        print("\n========== ALL CUSTOMERS ==========")
        service.display_customers()

    elif choice == "10":
        print("\nThank you for using Vehicle Rental Management System.")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 10.")
