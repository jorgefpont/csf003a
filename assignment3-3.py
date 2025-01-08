# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Question 3
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

"""
Write a recursive method that displays an integer value reversely.
For example, reverseDisplay(12345) will display 54321.
Prompt the user to enter an integer and call this method to
display its reversal
"""


def user_input():
    value = int(input("Enter a positive integer: "))
    # absolute value to ensure positive value
    return abs(value)


def reverseDisplay(value):
    # implement your code here
    # use end="" to avoid a newline after printing

    # base case, one digit, done as cannot reverse
    if value < 10:
        print(value, end="")
    else:
        # print the last digit of the number
        print(value % 10, end="")
        # remove the rightmost digit and recurse
        value = value // 10
        reverseDisplay(value)


def run():
    print("\n\n===== Question 3 =====")
    # implement your code here
    value = user_input()
    reverseDisplay(value)
    print()


run()
