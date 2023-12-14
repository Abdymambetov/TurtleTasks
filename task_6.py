import turtle

# Установка начальных координат
x, y = 0, 0

# Установка скорости движения
speed = 10

# Функция для перемещения влево
def move_left():
    global x
    x -= speed
    turtle.goto(x, y)

# Функция для перемещения вправо
def move_right():
    global x
    x += speed
    turtle.goto(x, y)

# Функция для перемещения вниз
def move_down():
    global y
    y -= speed
    turtle.goto(x, y)

# Инициализация окна turtle
turtle.speed(0)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(50)  # Создание круга

# Настройка обработчиков клавиш
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_down, "Down")

# Включение прослушивания клавиш
turtle.listen()

# Завершение работы при клике на окно
turtle.exitonclick()

