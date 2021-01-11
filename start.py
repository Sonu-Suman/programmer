import turtle
from turtle import *
import random
from pygame import mixer

# New Year Celebration code

mixer.init()
mixer.music.load('song-file_name.mp3')
mixer.music.play()

turtle.title("Happy new year")
turtle.hideturtle()
turtle.speed(10)
colors = ["red", "purple", "light green", "blue", "light blue", "pink", "deep pink", "white", "yellow"]
turtle.pencolor(random.choice(colors))
turtle.bgcolor("black")
n = 5

# Create FOR loop for STAR
for j in range(51):
    turtle.penup()
    turtle.goto(random.randint(-600, 600), random.randint(-300, 300))
    turtle.pendown()
    turtle.color(random.choice(colors))
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(18)
        turtle.right(144)
    turtle.end_fill()

# this is for crackers

for j in range(7):
    turtle.penup()
    turtle.goto(random.randrange(-500, 500, 100), random.randrange(-250, 250, 100))
    turtle.pendown()
    turtle.color(random.choice(colors))
    for x in range(60):
        turtle.begin_fill()
        forward(250)
        left(177)
        if abs(pos()) < 0.5:
            break
    turtle.end_fill()


turtle.penup()
turtle.goto(-300, 100)
turtle.pendown()
turtle.pencolor(random.choice(colors))
turtle.write("HAPPY NEW YEAR\n             2021", move=False, align="left", font=("italic", 51, "normal"))
mixer.music.stop()
turtle.done()
