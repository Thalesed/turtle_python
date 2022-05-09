import turtle

trt = turtle.Turtle()
bob = turtle.Turtle()

bob.goto(100, 0)

trt.speed(100)

bob.speed(100)

colors = ("red", "pink", "yellow", "purple", "blue", "green")
c = 0

while True:
    trt.color(colors[c%6])
    trt.circle(20)
    trt.penup()
    trt.left(90)
    trt.forward(10)
    trt.right(80)
    c+=1
    trt.pendown()

    bob.color(colors[c%6])
    bob.circle(20)
    bob.penup()
    bob.left(90)
    bob.forward(10)
    bob.right(80)
    bob.pendown()
    
turtle.done()
