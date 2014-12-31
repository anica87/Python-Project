'''
Created on Dec 30, 2014

@author: anicam
Python offers a datatype called set whose elements must be unique
It can be used to perform different  set operations like union, intersection, difference and symmetric difference

'''

E = {0, 2, 3, 4, 6, 8}
N = {1, 2, 3, 4, 5}


# set union
print ('Union of E and N is ', E|N)

# set intersection
print('Intersection of E and N is ', E&N)

# set difference
print ('Difference of E and N is ', E - N)

# set symmetric difference
print('Symmetric difference of E and N is ', E ^ N)