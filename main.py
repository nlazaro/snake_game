import turtle
import paddle
import ball
import time
import scoreboard

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

right_paddle = paddle.Paddle((350, 0))
left_paddle = paddle.Paddle((-350, 0))
scoreboard = scoreboard.Scoreboard()
ball = ball.Ball()

screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detects collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detects collision with r_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detects if ball misses
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()
