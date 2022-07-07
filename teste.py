import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = turtle.Turtle()

snake.color("white")
snake.forward(10)
snake.setheading(270)
snake.forward(10)
screen.update()



screen.exitonclick()