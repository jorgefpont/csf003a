# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Lab 4 Challenge 1, Number Analysis
# Due July 31, 2023
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

"""
Design a program that asks the user to enter a series of 20 numbers.
The program should store the numbers in a list then display the following data:
- The lowest number in the list
- The highest number in the list
- The total of the numbers in the list
- The average of the numbers in the list
"""


def user_input():
    nums = input("Enter a series of 20 numbers, separated by spaces: ")
    return nums


def run():
    nums = user_input()

    num_list = []
    # place input numbers into a list
    num_list = nums.split()

    # convert numbers in num_list to integers
    # need to use the index method to loop
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])

    print("Number list: ", num_list)
    print("Highest number: ", max(num_list))
    print("Lowest number: ", min(num_list))
    print("Sum of numbers: ", sum(num_list))
    print("Average of numbers", sum(num_list) / len(num_list))


run()
