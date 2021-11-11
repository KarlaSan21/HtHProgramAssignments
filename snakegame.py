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


 
# main game loop
while True:
    win.update()
    move()


