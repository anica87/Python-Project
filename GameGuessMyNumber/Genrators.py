import random


def lottery():
    # returns 6 numbers between 1 and 40
    for i in xrange(6):
        yield random.randint(1, 40)
    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)


for random_number in lottery():
    print "And the next number is ... %d!" % random_number


'''  Example 2 Using recursion'''    
def fib_two(n):
    if n == 1 or n == 2:
        return 1
   # print fib(n-1) + fib(n-2)
    return  fib_two(n-1) + fib_two(n-2)
    

print fib_two(6) 

'''  Example 1   Using looping technique'''
def fib_one(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a
print fib_one(6)
    
'''  Example 3 Using generators '''
a, b = 0, 1
def fib_three():
    global a, b
    while True:
        a, b = b, a+b
        yield a
f = fib_three()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()



        