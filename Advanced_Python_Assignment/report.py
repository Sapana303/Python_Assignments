from functools import wraps

from employee_processor import (
    employee_generator,
    filter_by_department,
    create_salary_filter,
)

## decorator
def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[Start] {func.__name__}")
        print(f"Generating Report...")

        result = func(*args, **kwargs)

        print(f"[END] {func.__name__}")

        return result

    return wrapper

## context manager
class ReportFile:

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


@log_execution
def generate_employee_report(employees, department, min_salary):

    employee_stream = employee_generator(employees)

    department_stream = filter_by_department(
        employee_stream,
        department
    )

    salary_filter = create_salary_filter(min_salary)

    with ReportFile("employee_report.txt") as report:

        report.write("Employee Report\n")
        report.write("===============\n")
        report.write(f"Department: {department}\n")
        report.write(f"Minimum Salary: {min_salary}\n")

        for employee in department_stream:

            if salary_filter(employee):

                line = (
                    f'{employee["id"]} - '
                    f'{employee["name"]} - '
                    f'{employee["department"]} - '
                    f'{employee["salary"]}\n'
                )

                report.write(line)

                print(line, end="")

    print("Report saved successfully.")