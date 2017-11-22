from turtle import *
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
    Turtle.__init__(self)
    register_shape("Rectangle",((0,0),(0,5),(25,5),(25,-5),(-25,-5),(-25,5),(0,5)))
    self.shape() 
        
    
