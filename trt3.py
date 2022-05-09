import turtle

trt = turtle.Turtle()

trt.getscreen().bgcolor("#994444")
trt.left(180)
trt.penup()
trt.forward(300)
trt.pendown()
trt.left(180)

trt.speed(100)

def star(num):
    global trt

    if num>10:
        for i in range(0, 5):
            trt.forward(num)
            trt.right(54+90)
            star(num/2)

star(400)     

turtle.done()
