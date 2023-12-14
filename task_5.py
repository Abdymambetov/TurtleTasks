import turtle


# Создаем экран
screen = turtle.Screen()
screen.bgcolor("white")

# Создаем черепашку
t = turtle.Turtle()
t.speed(2)  # Устанавливаем скорость черепахи

# Функция для рисования квадрата
def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

# Рисуем квадрат
draw_square(100)

# Закрываем окно при клике
screen.exitonclick()

