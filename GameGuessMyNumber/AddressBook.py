'''
Created on Dec 22, 2014

@author: anicam

The user wants to create an address book and downloads your program. How would  you make it? Create a program that prompts the user for the
information in most address address books and then stores it a .txt file!

regex uses for email validatior
dictionary structure uses for store a person with additional information

'''

import re
print 'AdressBook'

#Get the user's information'

forename = input('Enter the your forename: ')
lastname = input('Enter the your lastname: ')
email = input('Enter the your email: ')
phone = input('Enter the your phone number: ')


address_book_path = r'D:\python\adresses.txt'
address_book = {} # address book held in memory before dumped to file (baceno u fajl)
email_pattern = r'(\w[\w]*)@([\w]+\.[\w]+)'
record_delimiter = '|' # split name | email in file
 
 
def loadAddress():
#''' Load all address from file and places them in tuple in form (bool, list where the list is each row from the file(a person name | email))'''
    success, line = (False, [])
    try:
        f = open(address_book_path, 'r')
        lines = f.readlines()
        f.close()
        success, lines = (True, lines)
    except IOError  as e:
        print 'Error opening address books ', e
    return (success, line)

''' The latest style preference in Python is to use with statements for file handling, so that would
'''

