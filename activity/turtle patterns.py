# creating a polygon
import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()

s=6
s_len=70
a=360.0/s
# itrate loop for total number side
for i in range(s):
    polygon.forward(s_len)
    polygon.right(a)
turtle.done()