
import turtle
turtle.tracer(1,0)
turtle.addshape("beach.gif")
turtle.shape("beach.gif")
#turtle.forward(180)
#turtle.right(40)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(80)


for i in range(500):
    turtle.pendown()
    turtle.pencolor("blue")
    turtle.forward(180)
    turtle.right(40)
    turtle.pencolor("red")
    turtle.forward(100)
    turtle.right(90)
    turtle.pencolor("green")
    turtle.forward(80)
    turtle.penup()
    turtle.goto(0,0)
    turtle.right(1)
