# Foothill College
# CS 03A - Object Oriented Programming Methodologies in Python
# Question 1
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

"""
Define the Circle class that contains:
• Two data fields named x and y that specify the center of the circle
• A data field radius.
• An init method that creates a default circle with (0, 0) for (x, y) and 1 for radius.
• Accessors and mutators for all data fields
• A method getArea that returns the area of the circle.
• A method getPerimeter that returns the perimeter of the circle.
• A method containPoint(x, y) that returns true if the specified point (x, y) is inside this circle.
• A method containCircle(circle) that returns true if the specified circle is inside this circle.
• A method overlaps(circle) that returns true if the specified circle overlaps with this circle.

Once you have written the class, in the run method of q1.py, create four Circle instances of your choice
• print out the area and perimeter of each circle
• check if the point (5, 5) lies inside any of your circles
• check if any of your circles contains any other circle
• check if any of your circles overlaps any other circle
"""
import math


class Circle:
    # implement your code here

    # class variable
    PI = 3.14159265359

    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius

    # accessors
    def getCenter(self):
        return self.x, self.y

    def getRadius(self):
        return self.radius

    # mutators
    def setCenter(self, x, y):
        self.x = x
        self.y = y

    def setRadius(self, radius):
        self.radius = radius

    # other methods
    def getArea(self):
        area = Circle.PI * (self.radius ** 2)
        return area

    def getPerimeter(self):
        perimeter = 2 * Circle.PI * self.radius
        return perimeter

    # To find if a point is inside a circle:
    # find the distance between the point
    # and the center of the circle.
    # If the distance is less than the radius,
    # then the point is inside the circle
    def containPoint(self, x, y):
        x_c, y_c = self.getCenter()
        r_c = self.getRadius()
        d = math.sqrt((x_c - x) ** 2 + (y_c - y) ** 2)
        if d < r_c:
            return True
        else:
            return False

    # self is the reference circle
    # so Q is: is circle inside self?
    # If the distance between the centres plus
    # the smalle radius is less than the big radius,
    # then the small circle is inside the big circle
    def containCircle(self, circle):
        # dist bet centers
        x_ref, y_ref = self.getCenter()
        x, y = circle.getCenter()
        d = math.sqrt((x_ref - x) ** 2 + (y_ref - y) ** 2)
        r_ref = self.getRadius()
        r = circle.getRadius()
        if (d + r) < r_ref:
            return True
        else:
            return False

    # Check if 2 cicles overlap
    # if the distance bet the centers is less than
    # the sum of the radiuses and one does not contain
    # the other
    def overlaps(self, circle):
        x_ref, y_ref = self.getCenter()
        x, y = circle.getCenter()
        d = math.sqrt((x_ref - x) ** 2 + (y_ref - y) ** 2)
        r_ref = self.getRadius()
        r = circle.getRadius()

        # one does not contain the other
        if (d + r) < r_ref or (d + r_ref) < r:
            return False
        # overlap
        elif d < (r + r_ref):
            return True
        else:
            return False


def run():
    print("\n===== Question 1 =====\n")
    # implement your code here

    # define 4 circles
    c1 = Circle(x=0, y=0, radius=4)
    c2 = Circle(x=1, y=1, radius=10)
    c3 = Circle(x=5, y=5, radius=2)
    c4 = Circle(x=3, y=0, radius=4)

    # make a list of the 4 Circle objects above
    circle_list = [c1, c2, c3, c4]

    # print areas and perimeters
    for c in circle_list:
        print(f'center: {c.getCenter()}')
        print(f'radius: {c.getRadius()}')
        print(f'area: {c.getArea()}')
        print(f'perimeter: {c.getPerimeter()}')
        print()

    # check if the point (5, 5) lies inside any of your circles
    px = 5
    py = 5
    for c in circle_list:
        if c.containPoint(px, py):
            print(f'- Circle with center {c.getCenter()} and radius {c.getRadius()}\n contains point ({px}, {py})')

    print()

    # check if any of your circles contains any other circle
    cl = len(circle_list)

    for i in range(cl):
        for j in range(cl):
            if i != j:
                if circle_list[i].containCircle(circle_list[j]):
                    print(
                        f'- Circle with center {circle_list[i].getCenter()} and radius {circle_list[i].getRadius()}\ncontains circle with center {circle_list[j].getCenter()} and radius {circle_list[j].getRadius()}')

    print()

    # check if any of your circles overlaps
    # any other circle
    for i in range(cl):
        for j in range(i + 1, cl):  # i+1
            if circle_list[i].overlaps(circle_list[j]):
                print(
                    f'- Circle with center {circle_list[i].getCenter()} and radius {circle_list[i].getRadius()}\noverlaps with circle with center {circle_list[j].getCenter()} and radius {circle_list[j].getRadius()}')


run()
