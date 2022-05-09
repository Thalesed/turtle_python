import turtle

trt = turtle.Turtle()

#trt.circle(50)

trt.hideturtle()

trt.color('black','blue')
trt.begin_fill()
trt.penup()
trt.left(90)
trt.forward(100)
trt.pendown()

trt.goto(45, 75)
trt.goto(45, 25)
trt.goto(0, 0)
trt.goto(-45, 25)
trt.goto(-45, 75)
trt.goto(0, 100)

trt.penup()
trt.goto(0, 50)
trt.pendown()

trt.goto(-45, 75)
trt.goto(0, 50)
trt.goto(45, 75)
trt.goto(0, 50)
trt.goto(0, 0)
trt.goto(0, 50)

trt.end_fill()

trt.color('black', 'red')

trt.penup()
trt.goto(-22.5, 62.5)
trt.pendown()
trt.left(60)


trt.begin_fill()
for c in range(0, 30):
    trt.forward(94.25/90)
    trt.right(4)

for c in range(0, 15):
    trt.forward(282.74/90)
    trt.right(4)
    
for c in range(0, 30):
    trt.forward(94.25/90)
    trt.right(4)

for c in range(0, 15):
    trt.forward(282.74/90)
    trt.right(4)
trt.end_fill()
trt.right(60)

trt.penup()
trt.goto(-45, 50)
trt.pendown()

trt.begin_fill()

for c in range(0, 30):
    trt.forward(94.25/90)
    trt.right(4)

for c in range(0, 15):
    trt.forward(282.74/90)
    trt.right(4)
    
for c in range(0, 30):
    trt.forward(94.25/90)
    trt.right(4)

for c in range(0, 15):
    trt.forward(282.74/90)
    trt.right(4)

trt.end_fill()

trt.left(120)

trt.penup()
trt.goto(22.25, 12.125)
trt.pendown()

trt.begin_fill()

for c in range(0, 30):
    trt.forward(94.25/90)
    trt.right(4)

for c in range(0, 15):
    trt.forward(282.74/90)
    trt.right(4)
    
for c in range(0, 30):
    trt.forward(94.25/90)
    trt.right(4)

for c in range(0, 15):
    trt.forward(282.74/90)
    trt.right(4)

trt.end_fill()


turtle.done()
