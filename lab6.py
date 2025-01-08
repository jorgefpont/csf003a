# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Lab 6: Recursion for printing
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

"""
Write a recursive function that accepts an integer argument n.
The function should display n lines of asterisks on the screen,
with the first line showing 1 asterisk,
the second line showing 2 asterisks,
up to the n-th line which shows n asterisks.
"""


def asterisk(y, n):
    # base case
    if y > n:
        return
    # recursive case
    else:
        print(y * '*')
        asterisk(y + 1, n)


y = 1
n = int(input("Enter number of rows in tree\n"))

asterisk(y, n)
