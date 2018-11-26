'''
SC-100
Fall-2018
Tsagan Garyaeva
'''

#1

def initialLetterCount(wordList):
    dicCount={}
    for i in wordList:
        if i[0] not in dicCount:
            dicCount[i[0]]=1
        else:
            dicCount[i[0]]+=1
    return dicCount
horton = ['I','say','what','I','mean','and','I','mean','what','I','say']
print(initialLetterCount(horton))


#2

def initialLetters(wordList):
    dicCount={}
    for i in wordList:
        letter = i[0]; listLetter=i
        if letter not in dicCount :
            dicCount[letter] = [listLetter]
        if listLetter not in dicCount.values():
            dicCount[letter] = [listLetter]
        else:
            dicCount[letter].append(listLetter)
    return dicCount
    
print(initialLetters(horton))


#3

def shareALetter(wordList):
    words = {}
    for word in wordList:
        words[word] = [word]
 
    for lead_word in wordList:
        for word in wordList:
            if word == lead_word:
                continue
            else:
                for letter in word:
                    if letter in lead_word and word not in words[lead_word]:
                        words[lead_word].append(word)
 
    return words

print(shareALetter(horton))


#4

def wordLength(s):
    d={}
    for i in s.split():
        if len(i) not in d:
            for  y  in s.split():
                d[len(i)]= [i]
        else:
                d[len(y)]= [y]
       
    return d


s = 'one fish two fish red fish blue fish'
wl = wordLength(s)
print(wl)

