import turtle
from turtle import *
class Hexagon(Turtle):
    def __init__(self,size,color,speed):
        Turtle.__init__(self)
        self.home()
        self.color(color)
        self.speed(speed)
        self.begin_poly()
        self.left(30)
        self.fd(size)
        self.left(60)
        self.fd(size)
        self.left(60)
        self.fd(size)
        self.left(60)
        self.fd(size)
        self.left(60)
        self.fd(size)
        self.left(60)
        self.fd(size)
        self.left(60)
        self.end_poly()
        hexagon= self.get_poly()
        register_shape("leen",hexagon)
        self.shape("leen")
    def forward(self):
        self.fd(150)
l = Hexagon(100,"red",5)
l.forward()
import random
colormode(255)

class Square(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        #class body
        self.shapesize(size)
        self.shape("square")
    def random_color (self):
        a=random.randint(0, 255)
        b=random.randint(0, 255)
        c=random.randint(0, 255)
        self.color(a, b, c)

square1= Square(10)
square1.random_color()

class Rectangle(Turtle):
    def __init__(self,width,height):
        Turtle.__init__(self)
        self.width=width
        self.height=height
        register_shape("Rectangle",((0,0),(0,5),(25,5),(25,-5),(-25,-5),(-25,5),(0,5)))
        self.shape()
rec1= Rectangle(5,10)
rec1.shape()

