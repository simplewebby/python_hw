"""
CS 100 2018F Section 01
HW 1, Sep 7, 2018
"""

#2
 grades = ['A','B', 'C','F', 'F', 'B', 'A']
>>> gradeA = grades.count('A')
>>> frequency = [ grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F')]
>>> frequency
[2, 2, 1, 0, 2]

#3
 
>>> dog_breeds = ['collie','sheepdog','Chow','Chihuahua']
>>> herding_dogs = dog_breeds[:2]
>>> herding_dogs
['collie', 'sheepdog']

>>> tiny_dogs = dog_breeds[2:]
>>> tiny_dogs
['Chow', 'Chihuahua']
>>> dog_breeds is 'Persian'
False
