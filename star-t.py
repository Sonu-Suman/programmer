import turtle

#  CREATING A STAR
turtle.bgcolor("black")
# number of sides
n = 60

# Creating instance of turtle
pen = turtle.Turtle()

pen.begin_fill()
pen.color("red")
# loop to draw a side
for i in range(n):
    # drawing a side of length i*10
    pen.forward (i*10)
    # changing side of pen by 144 degree in clockwise
    pen.right(144)

pen.end_fill()
# Closing the instance
turtle.done()
