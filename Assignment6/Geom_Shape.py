#name: Shubham Rajkumar Somwanshi
#MIS: 111903102

import turtle
import time
s = turtle.getscreen()
t = turtle.Turtle()

class shape:
    def __init__(self, sides = 0, length = 0, breadth = 0) :
        self.sides = sides
        self.length = length
        self.breadth = breadth
    def info(self):
        print("In geometry, a shape can be defined as the form of an object or its outline, outer boundary or outer surface")

class point(shape):
    def info(self):
        print("A point in geometry is a location")
    def show(self):
        t.dot(0)

class line(shape):
    def info(self):
        print("Line is Collection of points that extends infinitely in two directions")
    def show(self):
        t.fd(100)
        t.bk(50)

class linesegment(shape):
    def info(self):
        print("Line Segment is Collection of points of fixed length")
    def show(self):
        t.fd(self.length) 

class polygon(shape):
    def info(self):
        print("Polygon is a shape having Sides")

class triangle(polygon):
    def trinfo(self):
        print("Triangle is a polygon having 3 sides")
    def show(self):
        for i in range(3):
            t.fd(self.length)
            t.left(120)
        
class paralleogram(shape):
    def info(self):
        print("Parallelogram is 4 sided shape having equal and parallel sides")
    def show(self):
        for i in range(2):
            t.fd(self.length)
            t.rt(45)
            t.fd(self.breadth)
            t.rt(135)

class rectangle(shape):
    def info(self):
        print("Rectangle is Paralleogram having ")
    def show(self):
        for i in range(2):
            t.fd(self.length)
            t.rt(90)
            t.fd(self.breadth)
            t.rt(90)
            

class square(polygon):
    def info(self):
        print("Square is a polygon having 4 sides")
    def show(self):
        for i in range(4):
            t.fd(self.length)
            t.rt(90)
            

class pentagon(polygon):
    def info(self):
        print("Pentagon is a polygon having 5 sides")
    def show(self):
        for i in range(5):
            t.fd(self.length)
            t.rt(72)

class hexagon(polygon):
    def info(self):
        print("Hexagon is polygon having 6 sides")
    def show(self):
        for i in range(6):
            t.fd(self.length)
            t.rt(60)

class heptagon(polygon):
    def info(self):
        print("Heptagon is polygon having 7 sides")
    def show(self):
        for i in range(7):
            t.fd(self.length)
            t.rt(51.42)

class octagon(polygon):
    def octinfo(self):
        print("Octagon is polygon having 8 sides")
    def show(self):
        for i in range(8):
            t.fd(self.length)
            t.rt(45)

class nonagon(polygon):
    def octinfo(self):
        print("Nonagon is polygon having 9 sides")
    def show(self):
        for i in range(9):
            t.fd(self.length)
            t.rt(40)

class decagon(polygon):
    def octinfo(self):
        print("Decagon is polygon having 10 sides")
    def show(self):
        for i in range(10):
            t.fd(self.length)
            t.rt(36)

class circle(shape):
    def info(self):
        print("A circle is all points in the same plane that lie at an equal distance from a center point")
    def show(self):
        t.circle(self.length, 360)
        
s1 = shape()
s1.info()
time.sleep(1)

# point
p1 = point(0, 100)
p1.show()
time.sleep(1)
t.reset()


# line
l1 = line(1, 200)
l1.show()
time.sleep(1)
t.reset()


# line Segment
l2 = linesegment(1, 200)
l2.show()
time.sleep(1)
t.reset()


# Parallelogram
para1 = paralleogram(4, 100, 60)
para1.show()
time.sleep(1)
t.reset()


# rectangle
rect1 = rectangle(4, 200, 100)
rect1.show()
time.sleep(1)
t.reset()


#triangle
tria1 = triangle(3, 100)
tria1.show()
time.sleep(1)
t.reset()


# square
sq1 = square(4, 100)
sq1.show()
time.sleep(1)
t.reset()


# pentagon
pen1 = pentagon(5, 100)
pen1.show()
time.sleep(1)
t.reset()


# hexagon
hex1 = hexagon(6, 100)
hex1.show()
time.sleep(1+1)
t.reset()


# octagon
oct1 = octagon(8, 100)
oct1.show()
time.sleep(1)
t.reset()


# nonagon
non1 = nonagon(9, 100)
non1.show()
time.sleep(1)
t.reset()


# decagon
dec1 = decagon(10, 100)
dec1.show()
time.sleep(1)
t.reset()


# circle
cir1 = circle(0, 100)
cir1.show()
time.sleep(1)
t.reset()