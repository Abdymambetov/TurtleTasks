import turtle

# Создаем объект черепашки
t = turtle.Turtle()

# Задаем скорость
t.speed(2)

# Рисуем анимацию
for _ in range(36):
    # Рисуем внутренний круг
    t.forward(100)
    t.right(45)
    t.forward(100)
    t.right(45)
    t.forward(100)
    t.right(45)
    t.forward(100)
    t.right(45)

    # Поворачиваем для следующего внутреннего круга
    t.right(10)

    # Рисуем внешний круг
    t.penup()
    t.forward(40)
    t.pendown()
    t.circle(140)

    # Поворачиваем для следующего внешнего круга
    t.right(10)

# Завершаем программу
turtle.done()
