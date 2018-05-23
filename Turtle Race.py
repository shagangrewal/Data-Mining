from turtle import *
from random import randint

speed(100)
bgcolor('light blue')
penup()
goto(-275,275)
pendown()
write("Welcome to the Turtle Race",font=("Arial",24))
penup()
goto(-275,200)
pendown()
write(0)
for i in range(1,21):
    forward(25)
    write(i*5,align='center')
    

penup()
right(180)
forward(500)
left(90)
pendown()

for j in range(11):
    forward(200)
    backward(200)
    penup()
    left(90)
    forward(50)
    right(90)
    pendown()

a = Turtle()
a.penup()
a.goto(-275,180)
a.shape('turtle')
a.color('red')
for k in range(1,11):
    a.right(36)

b = Turtle()
b.penup()
b.goto(-275,150)
b.shape('turtle')
b.color('green')
for k in range(1,11):
    b.right(36)

c = Turtle()
c.penup()
c.goto(-275,120)
c.shape('turtle')
c.color('yellow')
for k in range(1,11):
    c.right(36)

d = Turtle()
d.penup()
d.goto(-275,90)
d.shape('turtle')
d.color('blue')
for k in range(1,11):
    d.right(36)

for i in range(165):
    a.forward(randint(1,5))
    b.forward(randint(1,5))
    c.forward(randint(1,5))
    d.forward(randint(1,5))




    
