import turtle

screen = turtle.Screen()

square_turtle = turtle.Turtle()

square_turtle.pencolor("blue")

for _ in range(4):
    square_turtle.forward(100)
    square_turtle.right(90)

square_turtle.penup()
square_turtle.goto(-50, 0)
square_turtle.pendown()

star_turtle = turtle.Turtle()

star_turtle.pencolor("red")

angle = 144

for _ in range(5):
    star_turtle.forward(100)
    star_turtle.right(angle)

screen.exitonclick()
