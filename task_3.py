import turtle
import random
# Создание экземпляра черепахи (героя игры)
hero = turtle.Turtle()
hero.shape("turtle")
hero.color("blue")
hero.penup()
# Создание препятствий
obstacles = []
def create_obstacle(x, y):
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.shapesize(stretch_wid=2, stretch_len=2)
    obstacle.penup()
    obstacle.goto(x, y)
    obstacles.append(obstacle)
# Генерация случайных препятствий
for _ in range(5):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    create_obstacle(x, y)
# Функции для перемещения героя
def go_up():
    hero.setheading(90)
    hero.forward(20)
    check_collision()
def go_down():
    hero.setheading(270)
    hero.forward(20)
    check_collision()
def go_left():
    hero.setheading(180)
    hero.forward(20)
    check_collision()
def go_right():
    hero.setheading(0)
    hero.forward(20)
    check_collision()
# Функция для проверки столкновений с препятствиями
def check_collision():
    for obstacle in obstacles:
        if hero.distance(obstacle) < 20:
            hero.goto(0, 0)  # Возвращаем героя в центр, если произошло столкновение
# Установка обработчиков клавиш
turtle.listen()
turtle.onkey(go_up, "Up")
turtle.onkey(go_down, "Down")
turtle.onkey(go_left, "Left")
turtle.onkey(go_right, "Right")
# Завершение работы при клике на окно
turtle.exitonclick()

