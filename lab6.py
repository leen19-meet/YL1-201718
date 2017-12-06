from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius= radius
        self.color(color)
        self.speed(speed)


def check_collision(ball1,ball2):
    a= ball1.radius+ball2.radius
    x1= ball1.xcor()
    x2= ball2.xcor()
    y1= ball1.ycor()
    y2= ball2.ycor()
    D=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
    if D<=a:
        print("the two circles collide")
    else:
        print("the two circles don't collide")

ball1= Ball(10,"red",10)
ball2= Ball(50,"blue",15)
ball2.penup()
ball1.penup
ball2.goto(100,100)



check_collision(ball1,ball2)



        
    
