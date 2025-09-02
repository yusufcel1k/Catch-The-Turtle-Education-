import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightblue3")
screen.title("Catch The Turtle")

t = turtle.Turtle()
t.turtlesize(3, 3)
t.shape("turtle")
t.color("green")

a = turtle.Turtle()
a.hideturtle()
a.penup()
a.goto(0, 300)

timer = 12

def countdown(s):
    global timer
    a.clear()
    if s > 0:
        a.write(f"Time: {s}", align="center", font=("Arial", 24, "bold"))
        timer = s
        turtle.ontimer(lambda: countdown(s-1), 1000)
    else:
        a.write("Finished!", align="center", font=("Arial", 24, "bold"))
        t.hideturtle()
        t.onclick(None)

countdown(timer)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 350)
score = 0

def score_update():
    pen.clear()
    pen.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

def click(x, y):
    global score
    if timer > 0:
        score += 1
        score_update()

def move():
    if timer > 0:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t.teleport(x, y)
        screen.ontimer(move, 500)

t.onclick(click)
score_update()
move()

turtle.done()