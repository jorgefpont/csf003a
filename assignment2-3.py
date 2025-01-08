# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Assignment 2-3
# Due July 31, 2023
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

"""
Write a program that asks the user for his or her name,
then asks the user to enter a sentence that describes himself or herself.
Once the user has entered the requested input,
the program should create an HTML file containing the input for a simple Webpage.
"""


def user_input_name():
    n = input("Enter your name: ")
    return n


def user_input_desc():
    n = input("Enter a sentence that describes you: ")
    return n


def run():
    print('\n2.4 html File')

    name = user_input_name()
    desc = user_input_desc()

    # Open the file for writing
    with open('my_page.html', 'w') as f:
        # Define the data to be written
        data = [
            '<html>',
            '<head>',
            '</head>',
            '<body>',
            '<center>',
            '<h1>',
            name,
            '</h1>',
            '</center>',
            '<p>',
            desc,
            '</p>',
            '</body>',
            '</html>']

        # Use a for loop to write each line of data to the file
        # source: from geeks for geeks lesson
        for line in data:
            f.write(line + '\n')


run()
