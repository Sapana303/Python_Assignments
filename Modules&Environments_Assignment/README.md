# Modules and Environments Assignment

This assignment demonstrates the use of Python modules, packages, virtual
environments, third-party libraries, and dependency management.

The assignment contains two independent Python projects:

- Project 1: `hr_report`
- Project 2: `employee_cli`

Both projects implement employee management functionality using Python
modules and packages. Each project has its own virtual environment and
uses different third-party libraries.

---

# 1. Project Structure

```text
Modules&Environments_Assignment/
│
├── README.md
│
├── hr_report/
│   │
│   ├── .venv/
│   │
│   ├── app.py
│   ├── requirements.txt
│   │
│   ├── templates/
│   │   └── employee_report.txt
│   │
│   └── employee_system/
│       ├── __init__.py
│       ├── employee.py
│       ├── salary.py
│       └── attendance.py
│
└── employee_cli/
    │
    ├── .venv/
    │
    ├── app.py
    ├── requirements.txt
    │
    └── employee_system/
        ├── __init__.py
        ├── employee.py
        ├── salary.py
        └── attendance.py
````

---

# 2. Project 1 - HR Report

The first project is `hr_report`.

It demonstrates:

* Python modules
* Python packages
* Virtual environments
* Jinja2
* PrettyTable
* Employee management
* Salary calculation
* Attendance management
* Template-based report generation
* Dependency management using `requirements.txt`

## Libraries Used

```text
Jinja2
PrettyTable
```

---

# 3. Project 2 - Employee CLI

The second project is `employee_cli`.

It demonstrates:

* Python modules
* Python packages
* Virtual environments
* Tabulate
* Rich
* Employee management
* Salary calculation
* Attendance management
* Command-line interaction
* Dependency management using `requirements.txt`

## Libraries Used

```text
Tabulate
Rich
```

---

# 4. What is a Module?

A module is a Python file that contains reusable Python code.

A module normally has a `.py` extension.

Examples from this project are:

```text
employee.py
salary.py
attendance.py
```

Each module is responsible for a particular part of the employee management
system.

```text
employee.py
    ↓
Employee information and employee operations

salary.py
    ↓
Salary and bonus calculations

attendance.py
    ↓
Attendance management
```

Modules make a program easier to organize, maintain, test, and reuse.

For example:

```python
from employee_system.employee import add_employee
```

The above statement imports the `add_employee()` function from the
`employee.py` module.

---

# 5. What is a Package?

A package is a directory that contains related Python modules.

In this assignment, `employee_system` is a package.

```text
employee_system/
│
├── __init__.py
├── employee.py
├── salary.py
└── attendance.py
```

The package groups related employee-management modules together.

The modules can be imported using the package name.

For example:

```python
from employee_system.employee import add_employee
from employee_system.salary import calculate_salary
from employee_system.attendance import mark_attendance
```

Therefore:

```text
employee_system
       ↓
    Package
       ↓
 ┌─────┼─────────────┐
 ↓     ↓             ↓
employee salary    attendance
  .py     .py          .py
```

The `__init__.py` file is included in the package.

---

# 6. What is a Virtual Environment?

A virtual environment is an isolated Python environment created for a
specific project.

It allows each project to maintain its own Python packages and package
versions.

For example, Project 1 has:

```text
hr_report/
└── .venv/
```

Project 2 has:

```text
employee_cli/
└── .venv/
```

The packages installed in one environment do not automatically become
available in the other environment.

This helps prevent dependency conflicts.

---

# 7. Why are Two Virtual Environments Used?

Two virtual environments are used because there are two independent
projects.

Project 1 uses:

```text
Jinja2
PrettyTable
```

Project 2 uses:

```text
Tabulate
Rich
```

Therefore:

```text
hr_report/
└── .venv/
    ├── Jinja2
    └── PrettyTable
```

and:

```text
employee_cli/
└── .venv/
    ├── Tabulate
    └── Rich
```

The two environments are isolated from each other.

This means that Project 1 can have its own dependencies while Project 2 can
have a different set of dependencies.

The main purpose is:

```text
Project 1
    ↓
Independent Environment
    ↓
Jinja2 + PrettyTable


Project 2
    ↓
Independent Environment
    ↓
Tabulate + Rich
```

This demonstrates environment isolation and independent dependency
management.

---

# 8. What is Jinja2 Used For?

Jinja2 is a template engine for Python.

In Project 1, Jinja2 is used to generate employee reports.

The project contains a template:

```text
templates/
└── employee_report.txt
```

The template can contain placeholders such as:

```text
Employee ID : {{ employee.id }}
Name        : {{ employee.name }}
Department  : {{ employee.department }}
Salary      : {{ employee.salary }}
```

Suppose the employee data is:

```python
employee = {
    "id": "E001",
    "name": "John",
    "department": "IT",
    "salary": 50000
}
```

Jinja2 replaces the placeholders with the actual values.

The generated report becomes:

```text
========================================
           HR EMPLOYEE REPORT
========================================

Employee Report
===============

Employee ID : E001
Name        : John
Department  : IT
Salary      : 50000
```

The basic flow is:

```text
Employee Data
      ↓
Jinja2 Template
      ↓
Generated Report
```

Jinja2 separates the report presentation from the Python application logic.

---

# 9. What is PrettyTable Used For?

PrettyTable is a Python library used to display data in formatted tables in
the terminal.

In Project 1, PrettyTable is used to display employee information.

Example output:

```text
+-------------+-------+------------+--------+
| Employee ID | Name  | Department | Salary |
+-------------+-------+------------+--------+
| E001        | John  | IT         | 50000  |
| E002        | Alice | HR         | 45000  |
| E003        | Bob   | Finance    | 55000  |
+-------------+-------+------------+--------+
```

PrettyTable makes employee information easier to read in the terminal.

The roles of Jinja2 and PrettyTable are different:

```text
Jinja2
    ↓
Generates reports from templates

PrettyTable
    ↓
Displays structured data as tables
```

---

# 10. What is Tabulate Used For?

Tabulate is a Python library used to create formatted tables from structured
data.

In Project 2, Tabulate is used to display employee and attendance
information.

Example employee table:

```text
+-------------+-------+------------+--------+
| Employee ID | Name  | Department | Salary |
+-------------+-------+------------+--------+
| E001        | John  | IT         | 50000  |
| E002        | Alice | HR         | 45000  |
| E003        | Bob   | Finance    | 55000  |
+-------------+-------+------------+--------+
```

Example attendance table:

```text
+-----+---------+
| Day | Status  |
+-----+---------+
| 1   | Present |
| 2   | Present |
| 3   | Absent  |
| 4   | Present |
+-----+---------+
```

The basic flow is:

```text
Python Data
     ↓
  Tabulate
     ↓
Formatted Table
```

---

# 11. What is Rich Used For?

Rich is a Python library used to create formatted and styled output in the
terminal.

In Project 2, Rich is used for:

* Application headings
* Panels
* Styled messages
* User prompts
* Formatted tables
* Command-line interface presentation

Example Rich panel:

```text
╭──────────────────── HR Management System ────────────────────╮
│                                                              │
│                  EMPLOYEE CLI APPLICATION                    │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
```

Rich can also display employee details:

```text
             Employee Details
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Field       ┃ Value      ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ Employee ID │ E001       │
│ Name        │ John       │
│ Department  │ IT         │
│ Salary      │ 50000      │
└─────────────┴────────────┘
```

The basic purpose of Rich is:

```text
Rich
  ↓
Styled CLI
  +
Panels
  +
Formatted Messages
  +
Rich Tables
```

---

# 12. Difference Between Jinja2, PrettyTable, Tabulate and Rich

| Library     | Project        | Main Purpose                             |
| ----------- | -------------- | ---------------------------------------- |
| Jinja2      | `hr_report`    | Generate template-based reports          |
| PrettyTable | `hr_report`    | Display formatted tables                 |
| Tabulate    | `employee_cli` | Display structured data as tables        |
| Rich        | `employee_cli` | Create styled terminal output and tables |

The overall design is:

```text
PROJECT 1
hr_report
    │
    ├── Jinja2
    │      ↓
    │   Employee Report
    │
    └── PrettyTable
           ↓
        Employee Table


PROJECT 2
employee_cli
    │
    ├── Tabulate
    │      ↓
    │   CLI Tables
    │
    └── Rich
           ↓
        Styled CLI
        Panels
        Rich Tables
```

---

# 13. Employee Module

Both projects contain an `employee.py` module.

The employee module handles employee information.

Example employee:

```python
{
    "id": "E001",
    "name": "John",
    "department": "IT",
    "salary": 50000
}
```

Typical operations include:

```text
add_employee()
get_employee()
get_all_employees()
```

`add_employee()` is used to add an employee.

`get_employee()` is used to find an employee using the employee ID.

`get_all_employees()` is used to retrieve all employees.

Keeping these operations inside `employee.py` follows the principle of
separating responsibilities into modules.

---

# 14. Salary Module

The `salary.py` module contains salary-related functionality.

Typical functions include:

```text
calculate_salary()
calculate_bonus()
```

Example:

```text
Basic Salary     = 50000
Bonus Percentage = 10%

Bonus            = 5000
Total Salary     = 55000
```

The salary calculation is kept in a separate module rather than placing
the complete logic inside `app.py`.

---

# 15. Attendance Module

The `attendance.py` module manages attendance.

Typical functions include:

```text
mark_attendance()
get_attendance()
calculate_attendance_percentage()
```

Example:

```text
Day 1 → Present
Day 2 → Present
Day 3 → Absent
Day 4 → Present
```

Attendance percentage:

```text
Present Days = 3
Total Days   = 4

Attendance Percentage
= (3 / 4) × 100
= 75%
```

The attendance functionality is kept separate from employee and salary
functionality.

---

# 16. What is requirements.txt?

`requirements.txt` is a text file that lists the Python packages required
by a project.

Each project has its own requirements file.

Project 1:

```text
hr_report/
└── requirements.txt
```

Project 2:

```text
employee_cli/
└── requirements.txt
```

Project 1 may contain dependencies such as:

```text
Jinja2==3.1.6
MarkupSafe==3.0.3
prettytable==3.18.0
wcwidth==0.8.2
```

Project 2 contains the dependencies required by the CLI project, such as:

```text
rich==<installed-version>
tabulate==<installed-version>
```

The exact package versions should be generated from the corresponding
virtual environment.

The requirements file can be installed using:

```powershell
pip install -r requirements.txt
```

This installs the dependencies listed in the file.

---

# 17. Why Should Package Versions Be Specified?

Package versions should be specified to make the project environment
reproducible.

For example:

```text
Jinja2==3.1.6
```

means that version `3.1.6` is required.

If we only write:

```text
Jinja2
```

pip may install a newer version when the environment is created in the
future.

A newer version may contain changes that affect the application's behavior.

Specifying versions helps with:

```text
1. Reproducibility
2. Dependency management
3. Compatibility
4. Consistent application behavior
5. Easier project setup
6. Easier maintenance
```

The idea is:

```text
requirements.txt
       ↓
Specified Versions
       ↓
Same Dependencies
       ↓
Reproducible Environment
```

---

# 18. Creating the Virtual Environment for Project 1

Navigate to the Project 1 directory:

```powershell
cd hr_report
```

Create the virtual environment:

```powershell
python -m venv .venv
```

Activate the environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the application:

```powershell
python app.py
```

---

# 19. Creating the Virtual Environment for Project 2

Navigate to Project 2:

```powershell
cd employee_cli
```

Create the virtual environment:

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the application:

```powershell
python app.py
```

---

# 20. Project 1 Example

After activating the `hr_report` environment:

```powershell
cd hr_report
.\.venv\Scripts\Activate.ps1
python app.py
```

The application can provide functionality such as:

```text
========================================
       HR REPORT GENERATOR
========================================

1. Display All Employees
2. Add Employee
3. Find Employee
4. Generate Employee Report
5. Salary Calculation
6. Attendance
7. Exit
```

Project 1 demonstrates:

```text
Python Modules
       ↓
Python Package
       ↓
Virtual Environment
       ↓
Jinja2
       ↓
PrettyTable
       ↓
Employee Management
       ↓
Salary Management
       ↓
Attendance Management
```

---

# 21. Project 2 Example

After activating the `employee_cli` environment:

```powershell
cd employee_cli
.\.venv\Scripts\Activate.ps1
python app.py
```

The application can provide functionality such as:

```text
╭──────────────────── HR Management System ────────────────────╮
│                  EMPLOYEE CLI APPLICATION                    │
╰──────────────────────────────────────────────────────────────╯

1. Display All Employees
2. Add Employee
3. Find Employee
4. Salary Calculation
5. Attendance
6. Exit
```

Project 2 demonstrates:

```text
Python Modules
       ↓
Python Package
       ↓
Virtual Environment
       ↓
Tabulate
       ↓
Rich
       ↓
Employee Management
       ↓
Salary Management
       ↓
Attendance Management
```

---

# 22. Checking Installed Packages

To check packages installed in the currently active environment:

```powershell
pip list
```

Another option is:

```powershell
pip freeze
```

For Project 1:

```powershell
cd hr_report
.\.venv\Scripts\Activate.ps1
pip list
```

For Project 2:

```powershell
cd employee_cli
.\.venv\Scripts\Activate.ps1
pip list
```

The output shows the packages installed in the active virtual environment.

---

# 23. Creating requirements.txt

To record installed packages and their versions:

```powershell
pip freeze > requirements.txt
```

For Project 1:

```powershell
cd hr_report
.\.venv\Scripts\Activate.ps1
pip freeze > requirements.txt
```

For Project 2:

```powershell
cd employee_cli
.\.venv\Scripts\Activate.ps1
pip freeze > requirements.txt
```

This records the installed package versions.

---

# 24. Recreating a Project Environment

A new developer can recreate the environment using the project files.

First create the environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Then run:

```powershell
python app.py
```

This provides a simple way to recreate the project environment.

---

# 25. Environment Isolation

The final environment structure is:

```text
Modules&Environments_Assignment/
│
├── hr_report/
│   │
│   ├── .venv/
│   │   ├── Jinja2
│   │   └── PrettyTable
│   │
│   └── requirements.txt
│
└── employee_cli/
    │
    ├── .venv/
    │   ├── Tabulate
    │   └── Rich
    │
    └── requirements.txt
```

The two projects do not use the same virtual environment.

This provides:

```text
Project 1
    ↓
hr_report/.venv
    ↓
Jinja2 + PrettyTable


Project 2
    ↓
employee_cli/.venv
    ↓
Tabulate + Rich
```

---

# 26. Final Comparison

| Feature              | Project 1           | Project 2            |
| -------------------- | ------------------- | -------------------- |
| Project Name         | `hr_report`         | `employee_cli`       |
| Virtual Environment  | `.venv`             | `.venv`              |
| Environment Location | `hr_report/.venv`   | `employee_cli/.venv` |
| Python Package       | `employee_system`   | `employee_system`    |
| Employee Module      | `employee.py`       | `employee.py`        |
| Salary Module        | `salary.py`         | `salary.py`          |
| Attendance Module    | `attendance.py`     | `attendance.py`      |
| Report Generation    | Jinja2              | CLI Output           |
| Table Library        | PrettyTable         | Tabulate             |
| CLI Styling          | Basic               | Rich                 |
| Main Libraries       | Jinja2, PrettyTable | Tabulate, Rich       |
| Dependency File      | `requirements.txt`  | `requirements.txt`   |
| Environment          | Independent         | Independent          |

---

# 27. Assignment Requirements Covered

This README covers all required documentation topics:

```text
1. What is a module?
       ↓
   Python file containing reusable code

2. What is a package?
       ↓
   Directory containing related Python modules

3. What is a virtual environment?
       ↓
   Isolated Python environment for a project

4. Why are two virtual environments used?
       ↓
   To keep the two independent projects and their dependencies isolated

5. What is Jinja2 used for?
       ↓
   Template-based employee report generation

6. What is PrettyTable used for?
       ↓
   Formatted employee tables

7. What is Tabulate used for?
       ↓
   Formatted CLI tables

8. What is Rich used for?
       ↓
   Styled terminal output and rich tables

9. What is requirements.txt?
       ↓
   File containing project dependencies

10. Why should package versions be specified?
        ↓
    Reproducible and consistent environments
```

---

# 28. Conclusion

This assignment demonstrates how Python applications can be organized using
modules and packages.

It also demonstrates the importance of virtual environments for isolating
project dependencies.

The two independent projects implement employee-management functionality
while using different third-party libraries.

Project 1 uses:

```text
Jinja2
PrettyTable
```

Project 2 uses:

```text
Tabulate
Rich
```

Each project has its own:

```text
Virtual Environment
requirements.txt
Application
employee_system Package
```

The overall concept demonstrated by this assignment is:

```text
                 Python Project
                       │
                       ↓
                    Package
                       │
             ┌─────────┼─────────┐
             ↓         ↓         ↓
          Module    Module    Module
             │
             ↓
      Virtual Environment
             │
             ↓
     Third-Party Libraries
             │
             ↓
       requirements.txt
             │
             ↓
   Reproducible Application
```

The assignment demonstrates practical use of:

```text
Modules
Packages
Virtual Environments
Jinja2
PrettyTable
Tabulate
Rich
requirements.txt
Package Versioning
Dependency Isolation
```
