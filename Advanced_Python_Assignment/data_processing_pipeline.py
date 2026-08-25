from employee_processor import EmployeeIterator
from report import generate_employee_report


employees = [
    {"id": 101, "name": "John", "department": "IT", "salary": 50000},
    {"id": 102, "name": "Mary", "department": "HR", "salary": 45000},
    {"id": 103, "name": "David", "department": "IT", "salary": 65000},
    {"id": 104, "name": "Sarah", "department": "Finance", "salary": 55000},
    {"id": 105, "name": "Alex", "department": "IT", "salary": 75000},
    {"id": 106, "name": "Lisa", "department": "HR", "salary": 48000},
]


def main():

    print("========== Employee Data Processing System ==========")

    department = input("Enter department: ").strip()

    min_salary = int(input("Enter minimum salary: "))

    generate_employee_report(
        employees,
        department,
        min_salary
    )


if __name__ == "__main__":
    main()