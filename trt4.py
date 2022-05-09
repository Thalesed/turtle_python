import turtle

trt = turtle.Turtle()

trt.speed(100)

colors = ["purple", "red", "green", "blue", "yellow"]

trt.pensize(10)

def bigstar(turtle, size):
    turtle.color(colors[size%5])
    turtle.forward(size)
    turtle.left(170)
    bigstar(turtle, size+1)

bigstar(trt, 10)
    

turtle.done()
