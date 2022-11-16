import time
from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Ping Pong")
screen.tracer(0)

paddle_1 = Paddle('right')
paddle_2 = Paddle('left')
ball = Ball()








screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")



game_on = True
while game_on:
    time.sleep(0.03)
    screen.update()
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with the paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 350 or ball.distance(paddle_2) < 50 and ball.xcor() < -350:
        ball.collision()


    ball.move()


screen.exitonclick()