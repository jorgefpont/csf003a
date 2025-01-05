# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Lab 3
# Due July 23, 2023
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

'''
Write a function named max that accepts two integer values as
arguments and returns the value that is the greater of the two.
For example, if 7 and 12 are passed as arguments to the function,
the function should return 12. Use the function in a program that
prompts the user to enter two integer values. The program should
display the value that is the greater of the two.
In your program, write the main function and calling your newly
created function in the main function.
'''


def max_num(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return 'both numbers are equal'


def user_input():
    try:
        x = int(input("Enter first integer: "))
        y = int(input("Enter second integer: "))
        return x, y
    except ValueError:
        print("an error ocured")
        exit()


def main():
    x, y = user_input()
    res = max_num(x, y)
    print(f"The largest number is: {res}")


main()
