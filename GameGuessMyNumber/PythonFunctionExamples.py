'''
Created on Dec 26, 2014

@author: anicam
'''
from future_builtins import ascii

# '''
# Python program to display powers of 2 using Anonymous Function 
# '''
# 
# # Take number of term from user
# number = int(raw_input('Enter a number: '))
# 
# #use annoymous function
# 
# result =  list(map(lambda i: pow(i,2), range(number)))
# # result =  list(map(lambda i: i ** 2, range(number))) both functions work
# for i in range(number):
#     print result[i]
# 
# power_of_number = lambda x: x ** 2
# print power_of_number(number)


'''
Python program to find numbers divisible by thirteen from a list using anonymous function 

'''
function =lambda x: x % 13 == 0
my_list = [12, 65, 54, 39, 102, 339, 221,]

result = list(filter(lambda x: x % 13 == 0, my_list))

'''
filter function returns  the items, if condition is true
'''
# display the result
print 'Numbers are divisible by 13 are ', result

# i = 0
# while i <len(my_list):
#     if(function(my_list[i]) == True):
#         print my_list[i], ' is  divisible by thirteen'
# #     else:
# #         print my_list[i], ' is not divisible by thirteen'
#     i+=1
#     

# '''
# Python program to convert decimal number into binary, octal and hexadecimal 
# '''
# 
# # Take decimal number from the user
# 
# dec = int(raw_input('Enter an integer number: '))
# 
# print 'decimal number is ', dec, 'binary is ', bin(dec),'octal is ', oct(dec), 'and hexadecimal is ', hex(dec)

# '''
# Python program to find ASCCI value of character
# 
# ord() inverse or contrary or opposite is chr()
# '''
# 
# character = raw_input('Enter a character: ')
# 
# print 'ASCCI value of character', character, 'is', ord(character)


# 
# '''
# Python program to find HCF or GCD 
# The highest common factor  or greatest common divisor (GCD) of two numbers  is the largest positive integer that
# perfectly divides the two given numbers. For example, The HCF of 12 and  14 is 2  
# '''
# 
# def HCF(x, y):
# #     smaller = NONE
#     if(x > y):
#         smaller = x
#     else:
#         smaller = y
#     for i in range(1, smaller + 1):
# # what is difference between range (number) ad range(number, number) BITNO
#         if(x % i == 0 and y % i == 0):
#             hcf = i
#     return hcf
# #             print 'THe HCF of numbers is ', i
# #         else:
# #             continue 
# # this part of code is unnecessary
# 
# x = int(raw_input('Enter a first number: '))
# y = int(raw_input('Enter a second number: '))
# 
# print("The H.C.F. of", x,"and", y,"is", HCF(x, y))
# 
# # HCF(x, y)
# 
# def euclidean_algorithm():
#     
#     while(y): #  condition is until y becomes zero
#         x, y = y, x  % y
#  # swapping values, in  each iteration we place the value of x in y and the remainder(x % y) in y,  simultaneously
#         return x


'''
Python program to find LCM
'''

def LCM(x, y):

    if(x > y):
        smaller = x
    else:
        smaller = y
    for i in range(1, smaller+1):
        print i
        if(x % i == 0 and y % i == 0):
            print i
            hcf = i
    return hcf

x = int(raw_input('Enter a first number: '))
y = int(raw_input('Enter a second number: '))
 
print("The H.C.F. of", x,"and", y,"is", LCM(x, y))
 

