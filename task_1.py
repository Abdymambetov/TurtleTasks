import turtle

screen = turtle.Screen()

star_turtle = turtle.Turtle()

star_turtle.pencolor("black")

star_turtle.pensize(2)

angle = 144

for _ in range(5):
    star_turtle.forward(100)
    star_turtle.right(angle)

screen.exitonclick()