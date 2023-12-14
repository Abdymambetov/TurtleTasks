import turtle
import random
# Создание экземпляра класса turtle.Turtle()
artist = turtle.Turtle()
# Функция для рисования многоугольника
def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        artist.forward(length)
        artist.left(angle)
# Функция для рисования галереи
def draw_gallery(num_shapes, sides_range, length_range):
    for _ in range(num_shapes):
        # Установка случайного числа сторон и длины для каждого многоугольника
        sides = random.randint(*sides_range)
        length = random.randint(*length_range)
        # Установка случайной позиции перед рисованием
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        artist.penup()
        artist.goto(x, y)
        artist.pendown()
        # Установка случайного цвета
        artist.color(random.random(), random.random(), random.random())
        # Рисование многоугольника
        draw_polygon(sides, length)
# Установка параметров для галереи
num_shapes = 5
sides_range = (3, 8)  # От 3 до 8 сторон
length_range = (50, 150)  # От 50 до 150 пикселей длина стороны
# Установка скорости рисования
artist.speed(2)
# Рисование галереи
draw_gallery(num_shapes, sides_range, length_range)
# Завершение работы при клике на окно
turtle.exitonclick()
