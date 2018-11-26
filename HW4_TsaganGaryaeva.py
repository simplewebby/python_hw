'''
CS-100 Fall 2018
HW-04
Tsagan Garyaeva
'''
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']
for i in range(len(months)):
    
    print(i+1 ,('J'+ months[i]))


for i in range(0,100):
    if((i % 2 == 0) or (i%5==0)):
        print(i,' ', end=' ')
        

        

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
empty =" "


for i in horton:
    if i[:] in vowels:
        empty = empty.join(i)
        print(empty, ' ', end=' ')

        


        


    

    
