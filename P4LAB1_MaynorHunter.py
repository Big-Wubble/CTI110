#Hunter M.
#7/4/2024
#P4LAB1
#Write a turtle graphics programs that draws a square using loops.

import turtle
tuck = turtle.Turtle()
tuck.shape("turtle")
tuck.color("blue")
tuck.pensize(5)


for f in range(4):
    tuck.forward(200)
    tuck.left(90)

chuck = turtle.Turtle()
chuck.shape("turtle")
chuck.color("red")
chuck.pensize(5)


for f in range(3):
    chuck.forward(200)
    chuck.left(120)

#turtle.left(90)
#turtle.forward(200)
    
turtle.exitonclick()
