import turtle
import time
import random

delay = 0.1
segments = []
score = 0
highScore = 0

# screen setup
win = turtle.Screen()
win.title("Snake")
win.bgcolor("green")
win.setup(width = 600, height = 600)
win.tracer(0)

# snake setup
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 100)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# score pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 -- High Score {}".format(highScore), align = "center", font = ("Courier", 24, "bold"))


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


# main game loop
while True:
    
    win.update()

    # eating food
    if head.distance(food) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # updating score
        score += 10
        if score > highScore:
            highScore = score

        # snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        new_segment.goto(head.xcor(), head.ycor())
        segments.append(new_segment)

    # moving snake body after head
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

        # moving snake body
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

    move()

    # head to body collisions
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # reseting snake body
            for segment in segments:
                segment.goto(10000, 10000)
            segments.clear()
            score = 0

    # border collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # reseting snake body
        for segment in segments:
            segment.goto(10000, 10000)
        segments.clear()
        score = 0

    
    

    # keyboard binds
    win.listen()
    win.onkey(go_up, "w")
    win.onkey(go_down, "s")
    win.onkey(go_right, "d")
    win.onkey(go_left, "a")
    time.sleep(delay)
    pen.clear()
    pen.write("Score: {} -- High Score {}".format(score, highScore), align = "center", font = ("Courier", 24, "bold"))


