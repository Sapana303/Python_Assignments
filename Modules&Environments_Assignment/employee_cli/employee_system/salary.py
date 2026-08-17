def calculate_salary(basic_salary, bonus=0):
    """
    Calculate total salary.

    Total salary = basic salary + bonus
    """
    return basic_salary + bonus


def calculate_bonus(basic_salary, bonus_percentage=10):
    """
    Calculate bonus based on a percentage of basic salary.
    """
    return basic_salary * bonus_percentage / 100