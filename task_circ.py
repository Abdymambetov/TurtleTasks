import turtle
t = turtle.Turtle()
speed = 10
t.speed(speed)
side_length = 100
for _ in range(4):
    t.forward(side_length)
    t.right(90)
t.penup()
t.goto(0, -50)
t.pendown()
radius = 50
t.circle(radius)
t.penup()
t.goto(t.xcor() - speed, t.ycor())
t.pendown()

# Рисуем окружность
t.circle(radius)

# Двигаем окружность вправо
t.penup()
t.goto(t.xcor() + speed, t.ycor())
t.pendown()

# Рисуем окружность
t.circle(radius)

# Двигаем окружность вниз
t.penup()
t.goto(t.xcor(), t.ycor() - speed)
t.pendown()

# Рисуем окружность
t.circle(radius)

# Завершаем программу
turtle.done()
