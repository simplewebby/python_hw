Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
"""
Tsagan Garyaeva
CS 100 2018F Section 01
HW 0, Sep 7, 2018

"""

# Exercise 5b 

days_in_year = 356
age = 35
gramms_in_kg = 1000


# Exercise 5c 

cost_per_pound_apple = 2.88
my_weight = 122.99
dim_to_ceiling = 8.3


# Exercise 5d 

my_name = 'Tsagan'
fav_color = 'black'
home_town = 'Howell'


# Exercise 5e
>>> song1 = ['na'] *17
>>> song1 [16] = 'Batman!'
>>> song1

# 6

"""
Exercise 1.1

1. In a print statement, what happens if you leave out one of the parentheses, or both?


a) When I did not put the parantheses it gave me : 

built-in function print>
b)  When I left just one paranthese it broght me to the nest line and expected my input.

2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?

a)  print('tsagan)
	  
SyntaxError: EOL while scanning string literal

b) print(tsagan)
	  
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(tsagan)
NameError: name 'tsagan' is not defined

3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
>>> 3++7
	  
10
>>> 2++2
	  
4
>>>


4. In math notation, leading zeros are ok, as in 02. What happens if you try this in Python?


>>> 02+9
	  
SyntaxError: invalid token
>>> 09
	  
SyntaxError: invalid token
>>> x = 09
	  
SyntaxError: invalid token
>>>



5. What happens if you have two values with no operator between them?


SyntaxError: invalid token
>>> 55
	  
55
>>> 55
	  
55
>>> 8
	  
8
>>> 9 9
	  
SyntaxError: invalid syntax
>>> 8 7
	  
SyntaxError: invalid syntax
>>>




Exercise 1.2. Start the Python interpreter and use it as a calculator.

1. How many seconds are there in 42 minutes 42 seconds?

>> 42*60
	  
2520
>>> 2520+42
	  
2562
>>>


2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.


>>> 10* 0.621371
	  
6.21371

3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

10km = 6.21371miles
42mins42sec = 42.7 mins

s = d/t
s= 6.21371 / 42.7 = 0.14 miles per min

>>> 6.2137/42.7
	  
0.145519906323185
>>>


 t = 2562 sec = 42.7mins / 60 = 0.71 hour
 
>>> 6.2137/0.71
	  
8.75169014084507 mph




Exercise 2.1. Repeating my advice from the previous chapter, whenever you learn a new feature,
you should try it out in interactive mode and make errors on purpose to see what goes wrong.


• We’ve seen that n = 42 is legal. What about 42 = n?


• >>> 42=n
	  
SyntaxError: can't assign to literal

How about  x = y = 1?


>>> x= y= 1
	  
>>> x
	  
1
>>> y
	  
1


• In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?



>>> print("hello");
	  
hello
>>> 2+3;
	  
5

• What if you put a period at the end of a statement?


>>> 3+5.
	  
8.0
>>> print('hello').
	  
SyntaxError: invalid syntax
>>> 7/7.
	  
1.0
>>> 


• In math notation you can multiply x and y like this: xy. What happens if you try that in Python?


>>> x=3
	  
>>> y=3
	  
>>> xy
	  
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    xy
NameError: name 'xy' is not defined

Exercise 2.2. Practice using the Python interpreter as a calculator:

1. The volume of a sphere with


>>> print(4/3.0*math.pi*5**3)
	  
523.598775598298886



2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?


>>> book_price = 24.94
	  
>>> discount = 40
	  
>>> discount = book_price *(40/100)
	  
>>> discount_price =book_price - discount
	  
>>> shipping = 3 + (0.75 * (60 - 1))
	  
>>> whole_sale = discount_price *60 + shipping
	  
>>> whole_sale
	  
945.09
>>> discount	  
9.976
>>> print(discount_price)
	  
14.964
>>> shipping
	  
47.25
>>> whole_sale
	  
945.09
>>> 


3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

start_time_hr = 6 + 52 / 60.0
easy_pace_hr = (8 + 15 / 60.0 ) / 60.0
tempo_pace_hr = (7 + 12 / 60.0) / 60.0
running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr-int(breakfast_hr))*60
breakfast_sec= (breakfast_min-int(breakfast_min))*60

print ('breakfast_hr', int(breakfast_hr) )
print ('breakfast_min', int (breakfast_min) )
print ('breakfast_sec', int (breakfast_sec) )















