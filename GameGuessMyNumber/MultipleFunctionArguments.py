'''
Created on Dec 22, 2014

@author: anicam
'''
def foo (first, second, third, *therset):
    print "First: %s" % first
    print "Second: %s" % second
    print "Third: % s" % third
    print "And all the rest ... %s" % list(therset)
''' The "therset" variable is a list of variables, which receives all arguments which were to the "foo" function after the first 3 arguments.
'''
    
foo(1, 2, 3, 4, 5)

''' It is also possible to send functions arguments by keyword, so that the order of the argument does not matter, using the following syntax:
'''
def bar(first, second,  third, **options):
    if options.get("action") == "sum":
        print "The sum is: %d" % (first + second + third)
    
    if options.get("number") == "first":
        return first
    if options.get("number") == "second":
        return 100

result = bar(1, 2, 3, action = "sum", number = "second")
print "Result: %d" %result

''' Fill in the foo and bar functions so they can receive a variable amount of arguments(3 or more). The foo function must return the amount of
 extra arguments received. The bar function must return true if the argument with the keyword magic number is worth 7 and False otherwise
'''

def foo_example(a, b, c, *args):  
    return len(args)
    
    
    
def bar_example(a, b, c, **magic_number):
    if magic_number.get("argument") == 7:
        return True
#     return False
    else:
        False
''' Za ovo sam glupa, proveriti '''
if foo_example(1,2,3,4) == 1:
    print "Good"

if foo_example(1,2,3,4, 5) == 2:
    print "Better"

if bar_example(1,2,3, argument = 7) == True:
    print "Great"
    
if bar_example(1,2,3,argument = 256) == False:
    print "Awesome"

if bar_example(1,2,3, argument = "string") == False:
    print "Awesome"


