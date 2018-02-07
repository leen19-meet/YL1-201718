from turtle import *
import turtle
import time
import random
import math
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()
writer= turtle.clone()
writer.penup()
writer.goto(250,250)
writer.pencolor("red")
writer.shapesize(100)
turtle.bgcolor("gold")
RUNNING = True
SLEEP = 0.05
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
MY_BALL = Ball(0,0,0,0,20,"red")
SCORE = 0
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 30
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_Dy = -5
MAXIMUM_BALL_Dy = 5

BALLS=[]

for i in range(NUMBER_OF_BALLS):
     x = random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS ,int(SCREEN_WIDTH)- MAXIMUM_BALL_RADIUS)
     y = random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS ,int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
     dx =random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
     dy =random.randint(MINIMUM_BALL_Dy, MAXIMUM_BALL_Dy)
     radius =random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
     color =(random.random(),random.random(),random.random())
     new_ball = Ball(x,y,dx,dy, radius, color)
     BALLS.append(new_ball)
     

def move_all_balls():
    for i in BALLS:
        i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
     if ball_a == ball_b:
          return False
     distance_x = ball_a.xcor() - ball_b.xcor()
     distance_y = ball_a.ycor() - ball_b.ycor()
     D=math.sqrt(math.pow(distance_x,2)+math.pow(distance_y,2))
     if D+10<=ball_a.r+ball_b.r:
          return True
     else:
          return False

def speed():
     for i in BALLS:
          i.dx+= 1
          i.dy+= 1

def check_all_balls_collision():
     for ball_a in BALLS:
          for ball_b in BALLS:
               if collide(ball_a,ball_b):
                    A_radius = ball_a.r
                    B_radius = ball_b.r
                    if A_radius > B_radius: #ball b is smaller
                         X_coordinate = random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS ,int(SCREEN_WIDTH)- MAXIMUM_BALL_RADIUS)
                         Y_coordinate = random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS ,int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
                         ball_b.goto(X_coordinate,Y_coordinate)
                         ball_b.dx =random.randint( MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                         ball_b.dy =random.randint( MINIMUM_BALL_Dy, MAXIMUM_BALL_Dy)
                         ball_b.r =random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                         color =(random.random(),random.random(),random.random())
                         ball_b.color(color)               
                         ball_a.r += 1
                         ball_a.shapesize(ball_a.r/10)
                         ball_b.shapesize(ball_b.r/10)
                    else: #ball a is smaller
                         ball_b.r += 1
                         X_coordinate = random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS ,int(SCREEN_WIDTH)- MAXIMUM_BALL_RADIUS)
                         Y_coordinate = random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS ,int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
                         ball_a.goto(X_coordinate,Y_coordinate)
                         ball_a.dx =random.randint( MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                         ball_a.dy =random.randint( MINIMUM_BALL_Dy, MAXIMUM_BALL_Dy)
                         ball_a.r =random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                         color =(random.random(),random.random(),random.random())
                         ball_a.color(color)               
                         ball_a.shapesize(ball_a.r/10)
                         ball_b.shapesize(ball_b.r/10)
     speed()
def gameOver():
     if check_myball_collision()== False:
          GM=turtle.clone()
          GM.penup()
          GM.goto(-320,-50)
          GM.write("GAME OVER" ,font=("David", 80, "normal"))
          GM.goto(-120,-80)
          GM.write("YOUR SCORE IS:" + str(SCORE),font=("David", 20, "normal"))
def check_myball_collision():
     global SCORE
     for ball in BALLS:
          if collide(ball,MY_BALL):
               ball_Radius = ball.r
               MY_BALL_Radius = MY_BALL.r
               if ball_Radius > MY_BALL_Radius:
                    return False

               else: #balls is smaller
                    SCORE += 1
                    MY_BALL.r += 1
                    MY_BALL.shapesize(MY_BALL.r/10)
                    X_coordinate = random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS ,int(SCREEN_WIDTH)- MAXIMUM_BALL_RADIUS)
                    Y_coordinate = random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS ,int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
                    ball.goto(X_coordinate,Y_coordinate)
                    ball.dx =random.randint( MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                    ball.dy =random.randint( MINIMUM_BALL_Dy, MAXIMUM_BALL_Dy)
                    ball.r =random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                    ball.color ((random.random(),random.random(),random.random()))               
                    ball.shapesize(ball.r/10)
     return True

         
def movearound(event):
     X_coordinate = event.x - round(SCREEN_WIDTH)
     Y_coordinate = round(SCREEN_HEIGHT) - event.y
     MY_BALL.goto(X_coordinate,Y_coordinate)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen() 
                         

while RUNNING:
     if (SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2):
          SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
          
     if (SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2):
          SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
     writer.clear()
     writer.write("SCORE:"+str(SCORE),font=("David", 12, "normal"))
     move_all_balls()
     check_all_balls_collision()
     gameOver()
     RUNNING = check_myball_collision()
     turtle.getscreen().update()
     time.sleep(SLEEP)
     print(SCORE)
turtle.mainloop()




     
               
    
