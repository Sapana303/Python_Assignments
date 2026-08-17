from jinja2 import Environment, FileSystemLoader
from prettytable import PrettyTable

from employee_system.employee import (
    add_employee,
    get_employee,
    get_all_employees
)

from employee_system.salary import (
    calculate_salary,
    calculate_bonus
)

from employee_system.attendance import (
    mark_attendance,
    get_attendance,
    calculate_attendance_percentage
)

# JINJA2 REPORT

def generate_employee_report(employee):
    environment = Environment(
        loader=FileSystemLoader("templates")
    )

    template = environment.get_template("employee_report.txt")

    return template.render(employee=employee)


# PRETTYTABLE

def display_employee_table():
    employees = get_all_employees()

    table = PrettyTable()

    table.field_names = [
        "Employee ID",
        "Name",
        "Department",
        "Salary"
    ]

    for employee in employees:
        table.add_row([
            employee["id"],
            employee["name"],
            employee["department"],
            employee["salary"]
        ])

    print(table)

# ADD EMPLOYEE

def add_employee_from_input():

    print("\n---------- Add Employee ----------")

    employee_id = input("Enter Employee ID: ").strip()

    # Check whether ID already exists
    if get_employee(employee_id):
        print("Employee ID already exists.")
        return

    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()

    while True:
        try:
            salary = float(input("Enter Salary: "))
            break
        except ValueError:
            print("Please enter a valid numeric salary.")

    employee = {
        "id": employee_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    add_employee(employee)

    print("\nEmployee added successfully!")
    print(employee)


# FIND EMPLOYEE

def find_employee():

    print("\n---------- Find Employee ----------")

    employee_id = input("Enter Employee ID: ").strip()

    employee = get_employee(employee_id)

    if employee:
        print("\nEmployee Found")
        print("----------------")
        print("ID         :", employee["id"])
        print("Name       :", employee["name"])
        print("Department :", employee["department"])
        print("Salary     :", employee["salary"])
    else:
        print("Employee not found.")


# GENERATE REPORT

def generate_report():

    print("\n---------- Generate Employee Report ----------")

    employee_id = input("Enter Employee ID: ").strip()

    employee = get_employee(employee_id)

    if employee:
        report = generate_employee_report(employee)
        print("\n" + report)
    else:
        print("Employee not found.")


# SALARY CALCULATION

def salary_calculation():

    print("\n---------- Salary Calculation ----------")

    employee_id = input("Enter Employee ID: ").strip()

    employee = get_employee(employee_id)

    if not employee:
        print("Employee not found.")
        return

    basic_salary = employee["salary"]

    try:
        bonus_percentage = float(
            input("Enter Bonus Percentage (default 10): ") or 10
        )
    except ValueError:
        print("Invalid bonus percentage.")
        return

    bonus = calculate_bonus(
        basic_salary,
        bonus_percentage
    )

    total_salary = calculate_salary(
        basic_salary,
        bonus
    )

    print("\nSalary Details")
    print("----------------")
    print("Employee       :", employee["name"])
    print("Basic Salary   :", basic_salary)
    print("Bonus          :", bonus)
    print("Total Salary   :", total_salary)


# ATTENDANCE

def attendance_menu():

    print("\n---------- Attendance ----------")

    employee_id = input("Enter Employee ID: ").strip()

    employee = get_employee(employee_id)

    if not employee:
        print("Employee not found.")
        return

    while True:

        print("\n1. Mark Present")
        print("2. Mark Absent")
        print("3. View Attendance")
        print("4. View Attendance Percentage")
        print("5. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            mark_attendance(employee_id, "Present")
            print("Attendance marked as Present.")

        elif choice == "2":

            mark_attendance(employee_id, "Absent")
            print("Attendance marked as Absent.")

        elif choice == "3":

            records = get_attendance(employee_id)

            if records:
                print("Attendance Records:", records)
            else:
                print("No attendance records found.")

        elif choice == "4":

            percentage = calculate_attendance_percentage(
                employee_id
            )

            print(
                "Attendance Percentage:",
                percentage,
                "%"
            )

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


# MAIN MENU

def main():

    while True:

        print("\n")
        print("=" * 45)
        print("           HR REPORT GENERATOR")
        print("=" * 45)

        print("1. Display All Employees")
        print("2. Add Employee")
        print("3. Find Employee")
        print("4. Generate Employee Report")
        print("5. Salary Calculation")
        print("6. Attendance")
        print("7. Exit")

        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            print("\n---------- Employee List ----------")
            display_employee_table()

        elif choice == "2":

            add_employee_from_input()

        elif choice == "3":

            find_employee()

        elif choice == "4":

            generate_report()

        elif choice == "5":

            salary_calculation()

        elif choice == "6":

            attendance_menu()

        elif choice == "7":

            print("\nThank you for using HR Report Generator.")
            break

        else:

            print("\nInvalid choice. Please select 1-7.")

# PROGRAM START

if __name__ == "__main__":
    main()