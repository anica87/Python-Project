'''
Created on Dec 22, 2014

@author: anicam

The user wants to create an address book and downloads your program. How would  you make it? Create a program that prompts the user for the
information in most address address books and then stores it a .txt file!

regex uses for email validatior
textwrap modul for formatting text paragraphs, functions are fill, wrap, indent deindent
dictionary structure uses for store a person with additional information

'''

import re
import textwrap

print 'AdressBook'

address_book_path = r'D:\python\adresses.txt'
address_book = {} # address book held in memory before dumped to file (baceno u fajl)
email_pattern = r'(\w[\w]*)@([\w]+\.[\w]+)'
record_delimiter = '|'
 # split name | email in file

record_delimiter = '|'
     
 
def loadAddress():
#''' Load all address from file and places them in tuple in form (bool, list where the list is each row from the file(a person name | email))'''
    success, line = (False, [])
    try:
        f = open(address_book_path, 'r')
        lines = f.readlines()
        f.close() # This line closes the file and clears the computer's memory
        success, lines = (True, lines)
        print success, line
    except IOError as e:
        print 'Error opening address books ', e
    return (success, line)

''' The latest style preference in Python is to use with statements for file handling, so that would become
'''



def main():

    (success, lines) = loadAddress()
    if not success:
        should_make_new_book = raw_input(textwrap.fill(''' You do not have 
an address book yet. 
                            Would you like to
create one?'''))
        if should_make_new_book in ('y', 'yes', 'ye'):
            f = open(address_book_path, 'w')
            f.close() # this is the reason why dictionary does not write in the file -- nije ovo resenje
            print 'New address book created', address_book_path
        # naredne 3 linije kod su mi nedostajale
        else:
            print 'Exiting'
            return
        
    else:
    # '''Now that we have the file loaded into memory, fill out the address book from file '''
        for line in lines:
            splitStr = line.split(record_delimiter)
            address_book[splitStr[0]] = splitStr[-1]
    # main input loop (break with 'q' or 'quit' during input)
    while True:
        new_person_name_input = raw_input('Enter the person forename(q/quit to stop): ')
        if new_person_name_input.lower() in ('q', 'quit'):
            break
        address_book[new_person_name_input] = new_person_name_input
        while True: #'''  loop until email is in valid format (x at y.z < mailto: a at y.z>)'''
            new_person_email_input = raw_input('Enter the person\'s email (q/quit to stop): ')
            match = re.search(email_pattern, new_person_email_input)
            if not match:
                print 'Email validation failed ... try again'
                continue
#  continue is not strictly needed here. but does make  the intent clear

            else:
                address_book[new_person_name_input] = new_person_email_input
                break # success
    record_addresses()
    print address_book
                    
def record_addresses():

    try:
        f = open(address_book_path, 'a')
    except IOError as e:
        print 'There is a error, we could not open the file', e
   
    
    for k, v in sorted(address_book.items()):
        f.write("{0}{1}{2} \n".format(k, record_delimiter, v))
    
    
        

"""  Should  have a  try in case the file failes to open
Also slightly more pythonic to do
for k, v in open(...):

There is no point, in sorting the data if  you are going to read it into a  dictionary. Python' dictionaries are unsorted 
(Unless you plan to reading the file manually - in a text editor say)

is there a better way to do this without placing a newline after each row
it is causing multiple line separators when writing back out to file 
(because  each time we finish reading, it ends with a trailing newline)
"""
main()               


'''
1.  sta uraditi ako ima fajl samo kreiran ali nemam nijednu osobu
2. ne upisuje u fajl  ime i email
'''

'''
raw_input() takes exactly what the user typed and passes it back (string)
input() take the raw_input() and performs an eval() on it as well. In actual fact:

input() <---> eval(raw_input())
eval() function - what does python's eval() do?
interprets string as code
eval evalutes expressions

'''