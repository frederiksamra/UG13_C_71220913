import turtle
t = turtle.Turtle()
s = turtle.Screen()

t.shape('turtle')
t.color('white')
s.bgcolor('blue')
t.pensize(20)
t.penup()
t.goto(-200,0)

t.pendown()
t.left(90)
t.forward(150)
t.right(90)
t.forward(80)
t.backward(80)
t.right(90)
t.forward(80)
t.left(90)
t.forward(80)
t.penup()

t.goto(0,0)
t.pendown()
t.left(90)
t.forward(150)
t.left(135)
t.forward(50)
t.penup()

t.goto(0,0)
t.pendown()
t.right(45)
t.forward(40)
t.left(180)
t.forward(80)
t.penup()

t.pensize(20)
t.goto(250,150)
t.pendown()
t.left(135)
t.forward(35)
for i in range(2):
    t.left(45)
    t.forward(50)
    t.left(45)
    t.forward(35)
t.forward(80)
for i in range(2):
    t.right(45)
    t.forward (35)
    t.right(45)
    t.forward (50)
t.penup()

t.goto(0,-100)
t.pendown()
t.right(135)
t.forward(80)
t.right(90)
t.forward(80)
t.right(90)
t.forward(80)
t.backward(80)
t.left(90)
t.forward(80)
t.right(90)
t.forward(80)
t.penup()

t.pensize(10)
t.goto(0,200)
t.pendown()
t.forward(40)
t.right(180)
t.forward(80)
t.left(90)
t.forward(80)
t.left(90)
t.forward(80)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)



s.exitonclick()

