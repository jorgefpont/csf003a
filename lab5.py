# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Lab 5 Capital Quiz
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

"""
Write a program that creates a dictionary containing the U.S. states as keys,
and their capitals as values. (Use the Internet to get a list of the states
and their capitals.) The program should then randomly quiz the user by
displaying the name of a state and asking the user to enter that state’s capital.
The program should keep a count of the number of correct and incorrect responses.
"""

import random

# I got this list of state-capitals
# from some website and copied it below

state_string = """Alabama, Montgomery,
Alaska, Juneau,
Arizona, Phoenix,
Arkansas, Little Rock,
California, Sacramento,
Colorado, Denver,
Connecticut, Hartford,
Delaware, Dover,
Florida, Tallahassee,
Georgia, Atlanta,
Hawaii, Honolulu,
Idaho, Boise,
Illinois, Springfield,
Indiana, Indianapolis,
Iowa, Des Moines,
Kansas, Topeka,
Kentucky, Frankfort,
Louisiana, Baton Rouge,
Maine, Augusta,
Maryland, Annapolis,
Massachusetts, Boston,
Michigan, Lansing,
Minnesota, Saint Paul,
Mississippi, Jackson,
Missouri, Jefferson City,
Montana, Helena,
Nebraska,Lincoln,
Nevada, Carson City,
New Hampshire, Concord,
New Jersey, Trenton,
New Mexico, Santa Fe,
New York, Albany,
North Carolina, Raleigh,
North Dakota, Bismarck,
Ohio, Columbus,
Oklahoma, Oklahoma City,
Oregon, Salem,
Pennsylvania, Harrisburg,
Rhode Island, Providence,
South Carolina, Columbia,
South Dakota, Pierre,
Tennessee, Nashville,
Texas, Austin,
Utah, Salt Lake City,
Vermont, Montpelier,
Virginia, Richmond,
Washington, Olympia,
West Virginia, Charleston,
Wisconsin, Madison,
Wyoming, Cheyenne"""

state_list = state_string.split(',')

# eliminate leading spaces and newline chars
for i in range(len(state_list)):
    state_list[i] = state_list[i].lstrip()

# turn the list into a dict.
# indices 0, 2, 4, ... are states
# indices 1, 3, 5, ... are the corresponding capitals
state_dic = {}
for i in range(0, len(state_list), 2):
    state_dic[state_list[i]] = state_list[i + 1]

right = 0
wrong = 0
again = 'y'

while again != 'n':
    # using method 1 in:
    # https://www.geeksforgeeks.org/python-get-random-dictionary-pair/
    res = state, capital = random.choice(list(state_dic.items()))

    guess = input(f'What is the capital of {state}? ')

    if guess.upper() == capital.upper():
        print("correct\n")
        right += 1
    else:
        print("wrong\n")
        wrong += 1

    again = input("Want to play again? (y/n): ")
    print()

    if again == 'n':
        print(f'correct = {right}\nwrong = {wrong}')
