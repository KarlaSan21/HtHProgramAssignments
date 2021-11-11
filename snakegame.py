import turtle

# screen setup
win = turtle.Screen()
win.title("my snake game")
win.bgcolor("blue")
win.setup(width = 600, height = 600)
win.tracer(0)

# snake setup
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

# main game loop
while True:
    win.update()



