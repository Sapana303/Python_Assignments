attendance_records = {}


def mark_attendance(employee_id, status):
    """
    Record attendance for an employee.

    status should be 'Present' or 'Absent'.
    """
    if employee_id not in attendance_records:
        attendance_records[employee_id] = []

    attendance_records[employee_id].append(status)

    return status


def get_attendance(employee_id):
    """
    Return all attendance records for an employee.
    """
    return attendance_records.get(employee_id, [])


def calculate_attendance_percentage(employee_id):
    """
    Calculate attendance percentage.
    """
    records = get_attendance(employee_id)

    if not records:
        return 0

    present_count = records.count("Present")

    return (present_count / len(records)) * 100