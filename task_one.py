import turtle

# Создаем объект черепашки
t = turtle.Turtle()

# Рисуем прямоугольник
side_length = 100

for _ in range(4):
    t.forward(side_length)
    t.right(90)

# Перемещаем черепашку
t.penup()
t.goto(0, -50)
t.pendown()

# Рисуем окружность
radius = 50
t.circle(radius)

# Завершаем программу
turtle.done()
