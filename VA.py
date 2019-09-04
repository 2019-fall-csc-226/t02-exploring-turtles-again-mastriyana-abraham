#Shoutout to trigonometry!!!!

import turtle

wn = turtle.Screen()

vidya_turtle = turtle.Turtle()
vidya_turtle.shape('turtle')
vidya_turtle.color('blue')

head = 0
pen = 10
vidya_turtle.setheading(head)
vidya_turtle.pensize(pen)
vidya_turtle.penup()
vidya_turtle.forward(100)
vidya_turtle.left(90)
vidya_turtle.forward(100)
vidya_turtle.left(135)
vidya_turtle.pendown()
vidya_turtle.forward(141)
vidya_turtle.right(90)
vidya_turtle.forward(141)
vidya_turtle.left(135)
vidya_turtle.penup()
vidya_turtle.forward(100)
vidya_turtle.left(90)
vidya_turtle.forward(100)

abeTurtle = turtle.Turtle()
abeTurtle.shape('arrow')
abeTurtle.color('orange')

head = 0
pen = 10
abeTurtle.setheading(head)
abeTurtle.pensize(pen)
abeTurtle.pensize(pen)
abeTurtle.penup()
abeTurtle.forward(100)
abeTurtle.right(-90)
abeTurtle.backward(100)
abeTurtle.right(135)
abeTurtle.pendown()
abeTurtle.backward(141)
abeTurtle.left(90)
abeTurtle.backward(141)
abeTurtle.right(135)
abeTurtle.penup()
abeTurtle.backward(50)
abeTurtle.right(90)
abeTurtle.backward(50)
abeTurtle.pendown()
abeTurtle.backward(100)

abeTurtle.penup()
abeTurtle.left(135)
abeTurtle.backward(70.5)

frameturtle = turtle.Turtle()
frameturtle.shape('classic')
frameturtle.color('red')
head = 0
pen = 5
frameturtle.penup()
frameturtle.forward(200)
frameturtle.left(90)
frameturtle.forward(120)
frameturtle.left(90)

for pixels in range(40):
    frameturtle.forward(10)
    frameturtle.stamp()

frameturtle.left(90)

for pixels in range(24):
    frameturtle.forward(10)
    frameturtle.stamp()

frameturtle.left(90)

for pixels in range(40):
    frameturtle.forward(10)
    frameturtle.stamp()

frameturtle.left(90)

for pixels in range(24):
    frameturtle.forward(10)
    frameturtle.stamp()

wn.exitonclick()