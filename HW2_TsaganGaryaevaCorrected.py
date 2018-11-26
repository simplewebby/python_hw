'''
CS 100 2018F Section 01
HW 2, Sep 12, 2018
'''
'\nCS 100 2018F Section 01\nHW 2, Sep 12, 2018\n'
import turtle
t = turtle.Turtle()
s = turtle.Turtle()
p = turtle.Turtle()
t.color("red")
t.width(10)
t.circle(100, 360, 3)
s.penup()
s.goto(0,150)
s.home()
s.goto(200, 0)
s.goto(100,0)
s.goto(350,0)
s.color("blue")
s.width(10)
s.pendown()
for i in [0,1,2,3]:
    s.fd(100)
    s.left(90)

	
p.penup()
p.goto(0,-300)
p.home()
p.goto(-300,0)
p.pendown()
p.color("pink")
p.width(15)
p.shape("turtle")
p.circle(100, 360, 5)

cc = turtle.Turtle()
cc.penup()
cc.color("yellow")
cc.width(5)
cc.goto(0,-400)
cc.goto(0,-400)
cc.goto(0,-300)
cc.goto(0,-350)
cc.pendown()
n =0
while n < 4:
    n=n+1
    cc.penup()
    cc.setpos(0, -n*50)
    cc.pendown()
    cc.circle(50*n)

	

	

import math
print(math.factorial(100))

print(math.log2(1000000))

print(math.gcd(63,49))

