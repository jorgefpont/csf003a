# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Assignment 2-2
# Due July 31, 2023
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

"""
Write a program with a function that accepts a string as an argument
and returns a copy of the string with the first character of each
sentence capitalized.
"""


def capitalize(a_string):
    # list of chas to trigger capitalization of next char
    splitters = ['.', '!', '?']
    # split the string into a list of words
    l = a_string.split()
    # capitalize the first letter of the first word in the list
    l[0] = l[0].capitalize()

    for i in range(len(l)):
        if l[i][-1] in splitters and i < (len(l) - 1):
            l[i + 1] = l[i + 1].capitalize()

    return ' '.join(l)


def run():
    print('\n2.3 Capitalize')
    user_input = input("Enter string: ")
    res = capitalize(user_input)
    print(res)


run()
