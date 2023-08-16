# let's draw some cool drawings with package Turtles!!

# Import Turtle
import turtle
import colorsys

# let's get a setup in turtle
turtle.pensize(4) #Pen size
turtle.color("black")

t = turtle.Turtle()
s = turtle.Screen().bgcolor("pink")  #Background color
t.speed(0)
n = 70
h = 0

for i in range (360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range (2):
        t.left(2)
        t.circle(100)