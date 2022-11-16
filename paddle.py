from turtle import Turtle


UP = 90
DOWN = 270
SPEED = 40
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=8,stretch_len=1)
        self.color("white")
        self.penup()
        if position.lower() == 'left':
            self.goto(-375,0)
        elif position == 'right':
            self.goto(370,0)




    def up(self):
        new_y = self.ycor() + SPEED
        old_x = self.xcor()
        self.goto(x=old_x , y= new_y)



    def down(self):
        new_y = self.ycor() - SPEED
        old_x = self.xcor()
        self.goto(x=old_x , y= new_y)

