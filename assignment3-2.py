# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Question 2
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

"""
In q2.py, before the run method, write an Employee class that keeps
data attributes for the following pieces of information:
Employee name, and Employee number

Next, write a class named ProductionWorker that is a subclass of the
Employee class.

The ProductionWorker class should keep data attributes for the following
information: Shift number (an integer, such as 1, 2, or 3), and Hourly pay rate

The workday is divided into two shifts: day and night. The shift attribute will
hold an integer value representing the shift that the employee works.
The day shift is shift 1 and the night shift is shift 2. Write the appropriate
accessor and mutator methods for each class.

Once you have written the classes, in the run method of q2.py, create an
object of the ProductionWorker class and prompts the user to enter data for
each of the object’s data attributes.
Store the data in the object, then use the object’s accessor methods to
retrieve it and display it on the screen
"""


# Implement your Employee class here
class Employee:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def setName(self, name):
        self.name = name

    def setNumber(self, number):
        self.number = number


# Implement your ProductionWorker class here
# Employee pay rate and shift (1 or 2)
class ProductionWorker(Employee):

    def __init__(self, pay, shift, name, number):
        Employee.__init__(self, name, number)
        self.pay = pay
        self.shift = shift

    def getPay(self):
        return self.pay

    def getShift(self):
        return self.shift

    def setPay(self, pay):
        self.pay = pay

    def setShift(self, shift):
        self.shift = shift


def user_input():
    print("Enter the following employee data: ")
    employee_name = input("- Employee name (first last): ")
    employee_number = input("- Employee number: ")
    shift = int(input("- Shift number (1=day, 2=night): "))
    rate = float(input("- Hourly pay rate (without $): "))
    print()
    return employee_name, employee_number, shift, rate


def run():
    print("\n\n===== Question 2 =====")
    # implement your code here
    # get user input
    employee_name, employee_number, shift, rate = user_input()

    # Instantiate employee object
    employee = ProductionWorker(name=employee_name, number=employee_number, pay=rate, shift=shift)

    # print(employee_name, employee_number, shift, rate)\
    print("Employee Data:")
    print(f'Name: {employee.getName()}')
    print(f'Number: {employee.getNumber()}')
    print(f'Pay rate: ${employee.getPay()}')
    print(f'Shift: {employee.getShift()}')


run()
