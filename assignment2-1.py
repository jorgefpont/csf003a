# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Assignment 2-1
# Due July 31, 2023
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

'''
When an object is falling because of gravity,
the following formula can be used to
determine the distance the object falls in a specific time period:
d = 1/2 * g * t**2

The variables in the formula are as follows:
d is the distance in meters, g is 9.8, and t is
the amount of time, in seconds, that the object has been falling.

Write a function named falling_distance that accepts an object’s falling time
(in seconds) as an argument.
The function should return the distance, in meters, that the object
has fallen during that time interval.

Write a program that calls the function in a loop that passes the values
1 through 10 as arguments and displays the return value.
'''


def falling_distance(t):
    g = 9.8
    d = 1 / 2 * g * t ** 2
    return d


def run():
    print('\n2.1 Falling Object')
    for t in range(1, 11, 1):
        d = falling_distance(t)
        print(f'time {t} -- dist {d:.2f}')


run()
