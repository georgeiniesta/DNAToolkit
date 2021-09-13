#Pong game test

import turtle

wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("circle")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(50,0)






#Game loop
while True:
    wn.update()