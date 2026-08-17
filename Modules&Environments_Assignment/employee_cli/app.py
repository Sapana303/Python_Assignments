from tabulate import tabulate

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

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


# RICH CONSOLE
console = Console()


# DISPLAY ALL EMPLOYEES - TABULATE
def display_all_employees():
    employees = get_all_employees()

    if not employees:
        console.print("[yellow]No employees found.[/yellow]")
        return

    headers = [
        "Employee ID",
        "Name",
        "Department",
        "Salary"
    ]

    rows = []

    for employee in employees:
        rows.append([
            employee["id"],
            employee["name"],
            employee["department"],
            employee["salary"]
        ])

    print(
        tabulate(
            rows,
            headers=headers,
            tablefmt="grid"
        )
    )


# ADD EMPLOYEE
def add_employee_from_input():

    console.print(
        Panel(
            "Add New Employee",
            title="Employee Management"
        )
    )

    employee_id = console.input(
        "Enter Employee ID: "
    ).strip()

    # Check duplicate ID
    if get_employee(employee_id):
        console.print(
            "[red]Employee ID already exists.[/red]"
        )
        return

    name = console.input(
        "Enter Name: "
    ).strip()

    department = console.input(
        "Enter Department: "
    ).strip()

    while True:

        salary_input = console.input(
            "Enter Salary: "
        ).strip()

        try:
            salary = float(salary_input)
            break
        except ValueError:
            console.print(
                "[red]Please enter a valid numeric salary.[/red]"
            )

    employee = {
        "id": employee_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    add_employee(employee)

    console.print(
        Panel(
            f"Employee {employee_id} added successfully!",
            title="Success"
        )
    )


# FIND EMPLOYEE
def find_employee():

    console.print(
        Panel(
            "Find Employee",
            title="Employee Search"
        )
    )

    employee_id = console.input(
        "Enter Employee ID: "
    ).strip()

    employee = get_employee(employee_id)

    if not employee:
        console.print(
            "[red]Employee not found.[/red]"
        )
        return

    table = Table(title="Employee Details")

    table.add_column("Field")
    table.add_column("Value")

    table.add_row("Employee ID", employee["id"])
    table.add_row("Name", employee["name"])
    table.add_row("Department", employee["department"])
    table.add_row("Salary", str(employee["salary"]))

    console.print(table)


# SALARY CALCULATION
def salary_calculation():

    console.print(
        Panel(
            "Salary Calculation",
            title="Salary Management"
        )
    )

    employee_id = console.input(
        "Enter Employee ID: "
    ).strip()

    employee = get_employee(employee_id)

    if not employee:
        console.print(
            "[red]Employee not found.[/red]"
        )
        return

    basic_salary = employee["salary"]

    bonus_input = console.input(
        "Enter Bonus Percentage (default 10): "
    ).strip()

    try:
        bonus_percentage = (
            float(bonus_input)
            if bonus_input
            else 10
        )
    except ValueError:
        console.print(
            "[red]Invalid bonus percentage.[/red]"
        )
        return

    bonus = calculate_bonus(
        basic_salary,
        bonus_percentage
    )

    total_salary = calculate_salary(
        basic_salary,
        bonus
    )

    table = Table(title="Salary Details")

    table.add_column("Item")
    table.add_column("Amount")

    table.add_row(
        "Employee",
        employee["name"]
    )

    table.add_row(
        "Basic Salary",
        str(basic_salary)
    )

    table.add_row(
        "Bonus",
        str(bonus)
    )

    table.add_row(
        "Total Salary",
        str(total_salary)
    )

    console.print(table)


# ATTENDANCE MENU
def attendance_menu():

    console.print(
        Panel(
            "Attendance Management",
            title="Attendance"
        )
    )

    employee_id = console.input(
        "Enter Employee ID: "
    ).strip()

    employee = get_employee(employee_id)

    if not employee:
        console.print(
            "[red]Employee not found.[/red]"
        )
        return

    while True:

        console.print("\n[bold]Attendance Options[/bold]")

        console.print("1. Mark Present")
        console.print("2. Mark Absent")
        console.print("3. View Attendance")
        console.print("4. View Attendance Percentage")
        console.print("5. Back")

        choice = console.input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            mark_attendance(
                employee_id,
                "Present"
            )

            console.print(
                "[green]Attendance marked as Present.[/green]"
            )

        elif choice == "2":

            mark_attendance(
                employee_id,
                "Absent"
            )

            console.print(
                "[yellow]Attendance marked as Absent.[/yellow]"
            )

        elif choice == "3":

            records = get_attendance(employee_id)

            if not records:
                console.print(
                    "[yellow]No attendance records found.[/yellow]"
                )
            else:
                rows = []

                for day, status in enumerate(
                    records,
                    start=1
                ):
                    rows.append([
                        day,
                        status
                    ])

                print(
                    tabulate(
                        rows,
                        headers=["Day", "Status"],
                        tablefmt="grid"
                    )
                )

        elif choice == "4":

            percentage = calculate_attendance_percentage(
                employee_id
            )

            console.print(
                f"Attendance Percentage: "
                f"[bold]{percentage:.2f}%[/bold]"
            )

        elif choice == "5":
            break

        else:
            console.print(
                "[red]Invalid choice.[/red]"
            )


# MAIN MENU
def main():

    while True:

        console.print(
            Panel(
                "[bold]EMPLOYEE CLI APPLICATION[/bold]",
                title="HR Management System"
            )
        )

        console.print("1. Display All Employees")
        console.print("2. Add Employee")
        console.print("3. Find Employee")
        console.print("4. Salary Calculation")
        console.print("5. Attendance")
        console.print("6. Exit")

        choice = console.input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            console.print(
                "\n[bold]Employee List[/bold]\n"
            )

            display_all_employees()

        elif choice == "2":

            add_employee_from_input()

        elif choice == "3":

            find_employee()

        elif choice == "4":

            salary_calculation()

        elif choice == "5":

            attendance_menu()

        elif choice == "6":

            console.print(
                Panel(
                    "Thank you for using Employee CLI.",
                    title="Goodbye"
                )
            )

            break

        else:

            console.print(
                "[red]Invalid choice. Please select 1-6.[/red]"
            )


# PROGRAM START
if __name__ == "__main__":
    main()