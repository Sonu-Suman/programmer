import turtle
from turtle import *
import random
from pygame import mixer


# THIS IS CHRISTMAS WISHING GREETING 

mixer.init()
mixer.music.load('song-file_name.mp3')
mixer.music.play()

turtle.title("CHRISTMAS CELEBRATION")
turtle.screensize(600, 800)
turtle.bgcolor("#000000")
turtle.hideturtle()

# Christmas up side tree
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.pencolor("#ffffff")
turtle.begin_fill()
turtle.color("Green")
turtle.pensize(3)
turtle.circle(-200, steps=3)
turtle.end_fill()

#  Christmas tree downside
turtle.penup()
turtle.goto(0, -103)
turtle.pendown()
turtle.color("light green")
turtle.pensize(10)
turtle.setheading(270)
turtle.forward(150)

# 1).Turtle dot function
turtle.penup()
turtle.goto(-150, 250)
turtle.pendown()
turtle.dot(15, "pink")

# For loop for dot in the sky
for j in range(21):
    turtle.penup()
    turtle.goto(random.randint(-300, 300), random.randint(-400, 400))
    turtle.pendown()
    turtle.dot(random.randint(6, 15), random.choice(["red", "light green", "pink", "light blue", "white"]))


# 1).Christmas tree circle type bulb
turtle.penup()
turtle.goto(20, 25)
turtle.pendown()
turtle.pensize(1)
turtle.begin_fill()
turtle.color("red")
turtle.circle(10)
turtle.end_fill()

# 2).Christmas tree circle type bulb
turtle.penup()
turtle.goto(-120, -75)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(10)
turtle.end_fill()

# 1).Christmas tree square type bulb
turtle.penup()
turtle.goto(-65, 45)
turtle.pendown()
turtle.begin_fill()
turtle.color("Blue")
turtle.circle(10, steps=4)
turtle.end_fill()

# 2).Christmas tree square type bulb
turtle.penup()
turtle.goto(25, -90)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(90)
turtle.color("light blue")
turtle.circle(10, steps=4)
turtle.end_fill()

# 2).Christmas tree Triangle type bulb
turtle.penup()
turtle.goto(-35, -40)
turtle.pendown()
turtle.begin_fill()
turtle.color("deep pink")
turtle.circle(10, steps=3)
turtle.end_fill()

# 1).Christmas tree triangle type bulb
turtle.penup()
turtle.setheading(60)
turtle.goto(105, -90)
turtle.pendown()
turtle.begin_fill()
turtle.color("white")
turtle.circle(10, steps=3)
turtle.end_fill()

# 2).Christmas tree triangle type bulb
turtle.penup()
turtle.goto(25, 100)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(10, steps=3)
turtle.end_fill()


# 1). Christmas tree star type bulb
turtle.penup()
turtle.setheading(60)
turtle.goto(-15, 180)
turtle.pendown()
turtle.color('pink', 'Orange')
turtle.begin_fill()
for i in range(6):
    forward(50)
    right(160)
    if abs(pos()) < 1:
        raise i

turtle.end_fill()

for i in range(18):
    turtle.penup()
    turtle.pensize(1)
    turtle.goto(random.randrange(-150, 160, 20), random.randint(-101, -99))
    turtle.pencolor(random.choice(["light green", "light blue", 'red', "deep pink"]))
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(25)

mixer.music.stop()
turtle.done()
