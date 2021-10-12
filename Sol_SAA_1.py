import turtle

speed = 1
turtle.speed(speed)

for i in range(4):
    speed = speed + 1
    turtle.forward(200)
    turtle.left(90)
    turtle.speed(speed)
