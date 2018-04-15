from turtle import *
'''
wn = Screen()
wn.bgcolor("lightgreen")
alexa = Turtle()
alexa.speed(25)
for i in range(10,30):
    alexa.forward(i)
    alexa.left(89)
    alexa.stamp()

wn.exitonclick()'''


wn = Screen()
wn.bgcolor("lightgreen")
tess = Turtle()
tess.color("red")
tess.shape("turtle")

tess.up()                       # this is another way to pick up the pen
for i in range(1,100):      # start with dist = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.right(90)
    tess.forward(20)
    tess.stamp()
    tess.left(90)              # and turn her
    tess.forward(10)
    tess.left(180)
    tess.forward(40)
    tess.stamp()
    tess.right(90)
    tess.forward(20)
    tess.stamp()
wn.exitonclick()
