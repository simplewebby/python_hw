'''
CS-100
Fall -2018
Tsagan Garayeava
'''

#1

true_count = 0
false_count = 0
if False:
     true_count += 0
     false_count += 1
else:
     true_count += 2
     false_count += 2
if True and False:
     true_count += 0
     false_count += 4
elif not (True and False):
     true_count += 4
     false_count += 0
print(true_count, false_count)

###2
##nums = [-4, 0, 2]
##sum = nums[1] + nums[2] + nums[-4]
##print(sum)
# will give list index out of range error

#3
a_list = ['1:2', 3, [0]]
print(a_list[1:2])


#4
things = [1, -1, 0]
a = things[:1]
b = things[-3:]
print(a + b)

###5
##import turtle
##s = turtle.Screen()
##t = turtle.Turtle()
##for i in range(2):
##     t.forward(100)
##     t.right(90)
##     t.forward(100)


# this will draw a half of squre 

#6

def multiply(s):
    if len(s) > 0:
         start = s[0]
         end = s[-1]
    for letter in s:
         start += start
         end += end
    return start + end
newString = multiply("go")
print(newString)

#7
warming = True
hightide = False
if warming:
     print('oceans rise')
if not hightide:
     print('levees hold')
elif warming and hightide:
     print('Katrina')
else:
    print('category 1')

#8
awards = 'lalaland'
new = ''
for i in range(len(awards)-2):
    if awards[i] == awards[i+2]:
        new += awards[i]
    print(new)

#9
def operate(opA, opB):
    dups = 0
    for item in opA:
        if item not in opB:
            dups += 1
    return dups
    unique = 0
    for item in opA:
        if item in opB:
            unique += 1
    return unique
print(operate('hello', 'world'))


#10
def divvy(seq, number):
    less = 0
    more = 0
    for item in seq:
        if item < number:
            less += 1
        elif item > number:
            more += 1
        else:
            return None
    return less+more
print(divvy([5,-2,0,-2,1], -2))

#11A
import turtle
def midline(t, lineLength ):
    import turtle
    t = turtle.Turtle()
    t.pendown()
    t.fd(lineLength)

t =turtle.Turtle()
midline(t, 100)



#11B
import turtle

t = turtle.Turtle()
def spiral(t, length, multiplier, numlines, angle):
    t.down()
    for i in range(numlines):
        for i in range(0,180, angle):
            t.color('red')
            t.fd(length)
            t.setpos(0,0)
            t.left(angle)
            length=length*multiplier
        break
    

    for y in range(numlines):
        for y in range(0, 180, angle):
            t.color('blue')
            t.backward(length)
            t.setpos(0,0)
            t.right(angle)
            length=length/multiplier
        break
spiral(t, 50, 1.1, 15, 12) 






#12

def evenLengths(stringList):
    evenList=[]
    for word in stringList:
        if len(word) %2 == 0:
            evenList.append(word)
    return evenList
song = ['happy', 'birthday', 'to', 'you']
print(evenLengths(song))

#13

def courseLoad(light, heavy):
    number_credits = int(input('How many credits are you taking? '))
    if number_credits <= light:
        print(str(number_credits) + ' is a light schedule.')
        return 'light'
    if number_credits >=heavy:
        print(str(number_credits) + ' is a heavy schedule')
        return 'heavy'
    else:
        print(str(number_credits) + '  is an average schedule')
        return 'average'
mySchedule = courseLoad(11, 16)
print(mySchedule)

