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

# snake body
segments = []
new_segment = turtle.Turtle()
new_segment.speed(0)
new_segment.shape("square")
new_segment.color("gray")
new_segment.penup()
segments.append(new_segment)

for i in range(len(segments) - 1, 0, -1):
    x = segments[i - 1].xcor()
    y = segments[i - 1].ycor()
    segments[i].goto(x, y)

if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

def reset_segments():
    for segment in segments:
        segment.goto(10000,10000)
    segments.clear()

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

# main game loop
while True:
    
    if head.distance(food) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)

        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

    # border collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        reset_segments()

    # head collisions
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            reset_segments()
    
    win.update()
    move()
    time.sleep(delay)


