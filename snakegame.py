import turtle
import time
import random

# screen setup
win = turtle.Screen()
win.title("my snake game")
win.bgcolor("blue")
win.setup(width = 600, height = 600)
win.tracer(0)
delay = 0.1

# snake setup
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

# snake movement function
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# creating directions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

# keyboard binds
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")

# snake food
food = turtle.Turtle
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

if head.distance(food) < 15:
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)

# main game loop
while True:
    win.update()
    move()
    time.sleep(delay)


