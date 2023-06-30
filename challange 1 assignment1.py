import json


# Define the Employee class
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state


# Read the employee information from the JSON file
with open(r"C:\Users\valle\Assignment1\oops\employee data.py") as file:
    data = json.load(file)
    employee_list = []
    for employee_data in data["employees"]:
        employee = Employee(employee_data["Name"], employee_data["DOB"], employee_data["Height"], employee_data["City"],
                            employee_data["State"])
        employee_list.append(employee)

# Print the list of Employee objects
for employee in employee_list:
    print("Name:", employee.name)
    print("DOB:", employee.dob)
    print("Height:", employee.height)
    print("City:", employee.city)
    print("State:", employee.state)
    print()