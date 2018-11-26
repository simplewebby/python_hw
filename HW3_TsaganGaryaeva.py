import turtle
import math

'''
CS 100 2018F Section 01
HW3 CS 100 2018F Section 01

'''
#1 
a= 3
b=4
c=5
if(a < b):
    print('OK')
elif(c<b):
    print('Ok')
elif((a+b)==c):
    print('OK')
elif(((math.sqrt(a))+(math.sqrt(b))) == math.sqrt(c)):
    print('OK')
else:
    print('NOT OK')


#3
def draw_shape():
    import turtle
    for i in range(3):
	    color = input('What color: ')
	    line_width = input('What line width: ')
	    line_len = input('What line lenght: ')
	    shape = input('Choose from line, triangle or square? ')
	    if(str(shape) == 'line'):
		    bob = turtle.Turtle()
		    bob.color(color)
		    bob.width(line_width)
		    bob.fd(int(line_len))
	    elif(str(shape) == 'triangle'):
		    bob1 = turtle.Turtle()
		    bob1.penup()
		    bob1.setpos(-300,0)
		    bob1.pendown()
		    bob1.color(color)
		    bob1.width(line_width)
		    bob1.circle(float(line_len), 360, 3)
	    elif(str(shape)== 'square'):
		    bob2 = turtle.Turtle()
		    bob2.penup()
		    bob2.setpos(300,0)
		    bob2.pendown()
		    bob2.color(color)
		    bob2.width(line_width)
		    bob2.fd(float(line_len))
		    bob2.left(90)
		    bob2.fd(float(line_len))
		    bob2.left(90)
		    bob2.fd(float(line_len))
		    bob2.left(90)
		    bob2.fd(float(line_len))
		    bob2.left(90)
		    bob2.fd(float(line_len))

	    else:
		    print('Something went wrong!')

			
draw_shape()





    
    
