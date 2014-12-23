'''
Created on Jul 15, 2014

@author: anicam
'''


import random

if __name__ == '__main__':
    pass

randomNumber = random.randint(1,100)
print(randomNumber)
numberOfUser = input("Guess a number between 1 and 100: ")

while numberOfUser != randomNumber :
    
    if numberOfUser < randomNumber:
        print("Your number is to low, try again")
        numberOfUser = input("Guess a number between 1 and 100: ")
        
    elif numberOfUser > randomNumber:
        print("Your number is to high, try again")
        numberOfUser = input("Guess a number between 1 and 100: ")       
    else:
       
        break
    print("Congratulation")

'''Example one'''
list1= ['a', 'b', 'c', 'd', 'e']

print list1[10:]

''' The above code will output [] and will not result in an IndexError
As one would expect, attempting to access a member of a list using an index that exceeds the number of members
(e.g., attempting to access list[10]  in the list above ) results is an IndexError. However, attempting to access a slice of
list at a starting index that exceeds the number of members in the list
will not result in an IndexError and will simply return an empty list
What makes this a particularly nasty gotcha is that it can lead to bugs that are really hard to track down since no error
is raised at runtime '''
    
'''Example two'''


def div1(x, y):
    print "%s/%s = %s" % (x, y, x/y)
    
def div2(x, y):
    print "%s//%s = %s" % (x, y, x//y)
    

div1(5, 2)
div1(5., 2)
div2(5,2)
div2(5.,2.)

''' 
In Python 2, the output of the above code will be:
5 / 2  = 2
5.0 / 2 = 2.5
5 // 2 = 2
5.0 // 2.0 = 2.0 
By default, Python 2 automatically performs integer arithmetic if both operators are integers
As a result, 5/2 yields 2, while 5./2 yields 2.5
Note that you can override this behavior in Python 2 by adding the following import:

from __future__ division

Also note that the "double slash" operator will always perform integer division, regardless  of the operand types.
That is why 5.0 //2.0  yields 2.0 even in Python 2

Python 3: However, does hot have the behavior; i.e it does not perform integer arithmetic if both operators are integers
Therefore, in Python 3, the output will be as follows:
5/2  = 2.5
5.0/2 = 2.5

5//2 = 2
5.0//2.0 = 2.0
'''

''' Example 3'''

def extendList(val, list_one=[]):
    list_one.append(val)
    return list_one

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')



print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s"% list3


'''
Many will mistakenly expect list1 to be equal to [10] and list3 to be equal to ['a'], thinking that the list arrument will be
set to its default value of [] each time extendLIst is called

However, what actually happens is that the new default list is created only once  when the function is defined.
and that same list is then used subsequently whenever extendList is invoked without the argument being specified.
This is because expressions in default arguments are calculated when the function is defined, not when it is called

list1 and list3 are therefore operating on the same default list, whereas list2 is operating on a separate list that is
created (by passing its own empty list as the value for the list parameter)

The definition of the extendList function could be modified as follows, though, to always being a new list when
no list argument is specified, which is more likely to have been the desired behavior


With this revised implementation, the output would be: '''


def extendListRevised(val, list_one=[]):
    if list_one is None:
        list_one =[]
    list_one.append(val)
    return list_one




''' example four '''
 
class ParentOne(object):
    x = 1
    
class Child1(ParentOne):
    pass

class Child2(ParentOne):
    pass

print ParentOne.x, Child1.x, Child2.x
Child1.x = 2
print ParentOne.x, Child1.x, Child2.x
ParentOne.x = 3
print ParentOne.x, Child1.x, Child2.x

'''
The output of the above code will be:
1 1 1
1 2 1
3 2 3

What confuses or surprises many about this is that the last line of output is 3 2 3 rather than 3 2 1
Why does changing the value of Parent.x also change the value of Child2.x,
 but at the same time not change the value of Child1.x?
 
 The key to the answer is that, in Python class variables are internally handled as dictionaries.
 If a variable names is not found in the dictionary of the current class, 
The class hierarchy (i.e., its parent classes)  are searched until the referenced variable name is found
(it the referenced variable name is not found in the class itself or anywhere in its hierarchy, an AttributeError occurs)

Therefore, setting x =1 in the Parent class makes the class variable x (with value of 1) referenceable in that class 
and any of its children. That is why the first print statement outputs 1 1 1 

Subsequently, if any of its child classes overrides that value(for example, when we execute the statement Child1.x = 2)

Finally ,if the value is then changed in the Parent (for example, when we execute the statement Parent.x = 3)
that change is reflected also by any children that have not yet  overridden value (which in this case would be Child2)

That is why  the third print statement outputs 3 2 3
 
'''

'''  example five '''


def multipliers():
    return [lambda x : i * x for i in range(4)]

print [m(2) for m in multipliers()]


''' The output of above code will be [6, 6, 6, 6] (not [0, 2, 4, 6])

The reason for this is that Python's closures are late binding. This means that the values of variables used in closures are
looked up at the time the inner function is called.
So as a result, when at the any functions returned by multipliers() are called, the value of i looked up in the surrounding
scope at that time. By then, regardless of which of the returned functions is called the for loop has completed and i 
is left with its final value of 3. Therefore, every returned function multiplies the value it is passed by3, so since
a value of 2 is passed in the above code, they  will return a value of 6(i.e  3X2)


Incidentally, as pointed out in  bla bla some link, there is a somewhat widespreared misconcerption that this has something
to do with lambdas, which is not create the case functions created with a lambda expression are in no way special and the
same behavior is exhibited by functions created using an  oridinary def. 

Bellow are few examples if ways ti circumvnet this issue:
One solution would be use a Python generator as follows:
 
   
'''

def multipliersONe():
    for i in range(4): yield lambda x: i * x

'''Another solution is to create a closure that binds immediately to its arguments by using a default argument.
For example, 
'''

def multiplinesTwo():
    return[lambda x, i=i: i * x for i in range(4)]        
    
'''Or alternatively, you can use the function.partial() function:'''

from functools import  partial
from operator import mul

def multipliersThree():
    return [partial(mul, i) for i in range(4)]

''' example six '''

list_example = [[]] * 5
list_example # output?
list_example[0].append(10)
list_example # output?
list[1].append(20)
list_example # output?
list_example.append(30)
list_example # output


''' Here's why
The first line of output is presumably intuitive and easy to understand i.e., list = [[]] * 5 simply creates a list 
of 5 lists
However, the key thing to understand here is that the statement list = [[]] * 5 does NOT create a list containing 5 
distinct lists. rather, it creates a list of 5 reference to the same list. With this understanding, we can better
understand the rest of output

list[0].append(10) appends 10 to the first list. But since all 5 lists refer to the same list, the output is:
[[10],[10],[10],[10],[10]]

Similarly, list[1].append(20) appends 20 to the second list.

In contrast, list.append(30) is appending an entirely new element to the "outer" list, which therefore yields the output:


'''



