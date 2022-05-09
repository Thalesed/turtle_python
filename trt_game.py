import turtle
from random import randint

screen = turtle.Screen()
screen.bgcolor('lightgreen')

#turtle.speed(10)

trt1 = turtle.Turtle()
trt1.hideturtle()
trt1.penup()
trt1.goto(-300, 100)
trt1.color('red')
trt1.shape('turtle')


trt2 = turtle.Turtle()
trt2.hideturtle()
trt2.penup()
trt2.goto(-300, -100)
trt2.color('blue')
trt2.shape('turtle')

trt1.showturtle()
trt2.showturtle()

trt = turtle.Turtle()
trt.hideturtle()
trt.pensize(10)
trt.penup()
trt.goto(300, -200)
trt.pendown()
trt.left(90)
for c in range(0, 100):
    trt.forward(2)
    trt.color('white')
    trt.forward(2)
    trt.color('black')
trt.write("Finish\nLine", font=24)
run = True
print(trt1.pos(),trt2.pos())

while run:
    trt1.forward(randint(1, 6))
    trt2.forward(randint(1,6))
    if trt1.pos()[0] >= 300:
        print("PLayer one won")
        run = False
    elif trt2.pos()[0] >= 300:
        print("Player two won")
        print(trt2.pos())
        run = False


turtle.done()
