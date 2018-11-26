'''
cakes = ['angel', 'devil', 'pound', 'cheese', 'birthday']
byIngredient = cakes[:4]
byOccasion = cakes[-1]
print(byIngredient + byOccasion)
'''
##a. SyntaxError: invalid syntax
##b. TypeError: can only concatenate list (not "str") to list
##c. angeldevilpoundcheesebirthday
##d. ['angel', 'devil', 'pound', 'cheese', 'birthday']
##e. none of the above

'''
aSequence = [-1, 0, 'str', '0']
sum = aSequence[0] + aSequence[-1]
print(sum)
'''
##a. -1
##b. '-1'
##c. Index Error: list index out of range
##d. TypeError: unsupported operand type(s) for +: 'int' and 'str'
##e. none of the above

'''
print(zero())
def zero():
    return 0
'''
##a. 0
##b. zero()
##c. 'zero()'
##d. NameError: name 'zero' is not defined
##e. none of the above


def plusAndMinus(sequence):
    returnVal = 0
    for num in sequence:
        returnVal += num
    return(returnVal)
print(plusAndMinus([-2, -1, 1, 2]))
##a) [-2, -1, 1, 2]
##b) 0
##c) [6]
##d) 6
##e) none of the above



boolExprs = [3 > 2, 0 == 0, True, False, True or False, not False]
trueCount = 0
for expr in boolExprs:
    if expr:
        trueCount += 1
print(trueCount)

##a. TypeError: unorderable types: int, bool()
##b. 3
##c. 4
##d. 5
##e. none of the above


def check(aList):
	for element in range(len(aList)):
		if str(aList[element]) == aList[element+1]:
			return True
	return False
arg = [0, '0', 1, '1']
matched = check(arg)
print(matched)
##a. True
##b. False
##c. True True
##d. True False True
##e. none of the above

def notIn(letter, wordList):
    rtnList = []
    for word in wordList:
        if letter not in word:
            rtnList.append(word)
    return rtnList
quote = ['round', 'up', 'the', 'usual', 'suspects']
print(notIn('e', quote))

##a. ['round']
##b. ['round', 'up', 'usual']
##c. []
##d. TypeError: argument of type 'int' is not iterable
##e. none of the above



import turtle
s = turtle.Screen()
t = turtle.Turtle()
for i in range(5):
    if i//4 == 0:
        t.forward(100)
        t.right(90)
# Hint: '//' is integer division
##a. two adjacent sides of a square
##b. three sides of a square
##c. a square
##d. ZeroDivisionError: division by zero
##e. none of the above



def rangeExample(aString, stop, interval):
    returnVal = ''
    myRange = range(1, stop, interval)
    for idx in myRange:
        returnVal += aString[idx]
    return returnVal
print(rangeExample('Do unto others', 13, 4))
##a. Dno
##b. otts
##c. ooe
##d. IndexError: index out of range
##e. none of the above

