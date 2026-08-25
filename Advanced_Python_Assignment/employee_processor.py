## iterator
class EmployeeIterator:
    def __init__(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.employees):
            raise StopIteration

        employee = self.employees[self.index]
        self.index += 1

        return employee

## generator
def employee_generator(employees):
    for employee in employees:
        yield employee

##closure
def filter_by_department(employees, department):
    for employee in employees:
        if employee["department"] == department:
            yield employee


def create_salary_filter(min_salary):
    def check(employee):
        return employee["salary"] >= min_salary

    return check