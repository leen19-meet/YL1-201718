from turtle import Turtle
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color(color)
        self.shape("square")
        self.shapesize(r/10)
        self.fillcolor("red")
    def move(self,screen_width,screen_height):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x + self.dx
        new_y = current_y + self.dy
        right_side_ball = new_x + self.r
        left_side_ball = new_x - self.r
        down_side_ball = new_y - self.r
        up_side_ball = new_y + self.r
        
        if (right_side_ball > screen_width):
            self.dx = -self.dx
            
        elif (left_side_ball < -screen_width):
            self.dx = -self.dx
            
        elif (down_side_ball < -screen_height):
            self.dy = -self.dy

        elif (up_side_ball > screen_height):
            self.dy = -self.dy
        else:
            self.goto(new_x,new_y)

