'''
CS-100
FALL 2018
HW 6

'''

#1
def twoWords(length,firstLetter):

    first_word = "" 
    second_word= ""

    while True:

        first_word = input('A ' + str(length) + '-letter word please: ')
        if length == len(first_word):
            break
    while True:
        second_word = input('A word beginning with ' + firstLetter+ ' please')
        if second_word[0] == firstLetter.upper() or second_word[0] == firstLetter.lower():
            break
    return [first_word,second_word]
print(twoWords(5,'T'))


#2

def twoWordsV2(length,firstLetter):

    first_word = "" 
    second_word= ""

    while length != len(first_word):
        
        first_word = input('A ' + str(length) + '-letter word please: ')
      
    if(first_word[0]!=firstLetter):
        second_word = input('A word beginning with ' + firstLetter+ ' please')
        
    return [first_word,second_word]
print(twoWordsV2(3,'S'))

#3

def enterNewPassword():

    while True: 
        password = input("Enter password: ")
        if len(password) <8 and any(c.isdigit() for c in password):
            print("Password is too short")
        if len(password) > 15:
            print("Password is too long")
        if sum(str.isdigit(c) for c in password) < 1:
            print("Password must contain at least one digit:")
        if any(c.isdigit() for c in password) == False:
            print("You have No Digits")
            
        else:
           print("Password is valid")
           return False
enterNewPassword()



