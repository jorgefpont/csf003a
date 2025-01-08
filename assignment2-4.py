# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Assignment 2-4
# Due July 31, 2023
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

"""
Write a program that asks the user to enter an integer greater than 1,
then displays all of the prime numbers that are less than or equal to the
number entered. The program should work as follows:

• Once the user has entered a number, the program should populate a list
with all of the integers from 2 up through the value entered.
• The program should then use a loop to step through the list.
The loop should pass each element to a function that displays
the element whether it is a prime number.
"""

'''
To test, the list of primes from 1-100 is:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
'''


def user_input():
    n = int(input("Enter an integer greater than 1: "))
    return n


# populate a list with all of the integers
# from 2 up through the value entered
# by the user
def make_test_list(n):
    test_list = list(range(2, n + 1))
    return test_list


# test if number is prime
# needs number and list of primes
# up to that number
def test_prime(n, plist):
    for p in plist:
        if n % p == 0:
            return False
    return True


def run():
    print('\n2.2 List Operations')

    # initial prime list
    plist = [2]

    n = user_input()
    test_list = make_test_list(n)

    for n in test_list:
        prime = test_prime(n, plist)
        if prime:
            plist.append(n)

    print(plist)


run()
