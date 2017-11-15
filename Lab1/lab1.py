#problem-1
name=input("write your name: ")
print(name*3)
print(name*100)

#problem-2
#part-1
number1=4
print(number1)

#part-2
number2= number1/2
print(number2)

#problem-3
list1=[1,2,3]
sum1=list1[0]+list1[1]+list1[2]
for item in list1:
    print(item) 
    print(item*2)
print(sum1)

#problem-4
import turtle
turtle.tracer(1,0)
turtle.begin_fill()
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.goto(100,0)
turtle.goto(0,0)
turtle.goto(0,100)
turtle.goto(100,100)
turtle.hideturtle()
turtle.end_fill()

turtle.reset()
turtle.hideturtle()
turtle.penup()
turtle.color("blue")
turtle.circle(80)
turtle.goto(100,50)
turtle.pendown()
turtle.circle(80)
turtle.color("black")
turtle.penup()
turtle.goto(300,50)
turtle.pendown()
turtle.circle(80)
turtle.color("red")
turtle.penup()
turtle.goto(500,50)
turtle.pendown()
turtle.circle(80)

turtle.color("yellow")
turtle.penup()
turtle.goto(150,25)
turtle.pendown()
turtle.circle(80)

turtle.mainloop()
