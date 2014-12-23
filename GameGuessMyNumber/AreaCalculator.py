'''
Created on Dec 22, 2014

@author: anicam

Overview
The user will be prompted with a menu where he/she will select a shape.
Then user will give the appropriate information needed to solve  for the area, and the computer will give the area
Hope you all have taken geometry!
'''

print "Area Calculation Program"
print 
print "1. Triangle"
print "2. Circle"
print "3. Rectangle"
print "4. Quit"

# shape = None
# Get the user's choice:'
shape = input("Please select a number 1-4:")

# Calculate the area:
while shape != 4:
    if shape  == 1:
        height = input("Please enter the height: ")
        width = input("Please enter the width of the base:")
        area = (height*width)*0.5
        print "The area is  %d" % area
        break
    if shape == 2:
        radius = input("Please enter the radius: ")
        area = 3.14159*(radius**2)
        print "The area is  %d" % area
        break
    if shape == 3:
        height = input("Please enter the height: ")
        width = input("Please enter the width:")
        area = height*width
        print "The area is  %d" % area
        break
# if shape == 4:
#     print "This is the end"
#     quit()

"""
Dodati za handler ako se doda broj veci do 4 ili ako  ubaci 4 da se pita da li zeli stvarno da izadje iz tog programa
Razlika izemedju print and return statement
exception handling ako   se ubaci string
kreirati funkciju koja ce  da ima return statement i vratice povrsinu a mi cemo da imamo samo jedan print
"""

'''
What is difference between range and xrange functions
Xrange is faster, because range creates a list, if you do range(1, 10000) it creates a list of memory with 10000 elements
xrange is a sequence object that evaluates lazily, only stores  the range params  and generate the numbers on demand
Xrange returns an iterator and only keeps one number in memory at a time. Range keeps tje entire list of numbers in memory

Note that in Python 3.0 there is only range and it behaves exactly like the 2.x.xrange


What is difference between single and double quota

Single and double quoted strings in Python are identical. The only difference is that single-quoted strings can contain unescaped double quota

Three double quotes to start and end multi-line strings

A switch-case statement is a useful programming language that lets you control the flow of the program based on value of a variable or expression.
In paricular, if the variable or expression that I am testing has a number of different of possible values, you could execute a block of code
for each separate value. 
The default case is executed when the value of the variable does not match anything for which a case is defined.
Notice that some cases have a break statement while others don't. If a particular case block is executed and no break is found, then all
the following case blocks will be executed until a break is found

One simple substitute is using a string of if-else block , with each if condition being what would have a matching case, but it is not a elegant 
solution

THe pythonic solution is to make use of Python's powerful dictionaries.
Also known as associative arrays in some languages. Python's dictionaries allow a simple one-to one matching of a key and a value.
When used a part of a switch case statement, the keys are what would normally trigger the case blocks.
The interesting part is that is values in dictionaries refer to functions that contain the code that would normally be inside the case blocks

'''


options = {0: 'zero', 1 :'sqr', 4: 'sqr', 9: 'sqr', 2: 'even', 3: 'prime', 5: 'prime', 7: 'prime' }

def zero():
    print "You typed zero. \n"

def sqr():
    print 'n is a perfect square \n'

def even():
    print 'n is an even number \n'

def prime():
    print 'n is a prime number \n'

print options[2]

