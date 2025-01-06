# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Lab 4 Challenge 2, Initials
# Due July 31, 2023
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

"""
Write a program that gets a string containing a person’s first, middle,
and last names, and displays their first, middle, and last initials.
For example, if the user enters John William Smith,
the program should display J. W. S.
"""


def user_input():
    full_name = input("Enter first, middle, and last name separated by spaces: ")
    return full_name


def run():
    full_name = user_input()

    split_name = []
    # put the name into a 3 element list of first, middle, last
    split_name = full_name.split()

    temp = []
    for word in split_name:
        # get first word of each list item, capitalize,
        # and add a period after
        temp.append(word[0].capitalize() + '.')

    print(temp)
    # join the 3 initials in the list into one string,
    # separated by spaces
    res = ' '.join(temp)
    print(res)


run()
