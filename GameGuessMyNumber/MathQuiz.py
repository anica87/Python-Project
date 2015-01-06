'''
Created on Jan 5, 2015

@author: anicam
'''

from random import randint
while True:
    correct = 0
    levels = {'beginner': 10, 'intermediate': 25, 'advanced': 100}
    questions = int(raw_input("How many times do you  want to answer on questions? "))
    level =raw_input("Choose a level: beginner, intermediate, advanced ")
    for i in range(questions):
        n1 = randint(1, levels[level])
        n2 = randint(1, levels[level])
        prod = n1 * n2
         
        ans = input("What' s %d times %d " % (n1, n2))
        if ans == prod:
            print "That is right --- well done.\n"
            correct = correct + 1
        else:
            print "No, I'm afraid the answer is %d.\n" % prod
             
    print "\n I asked you %d questions. You got %d of them right" % (questions, correct)
    third = questions/3
    if correct in (0, third):
        print "Please ask your math teacher for help!"
    elif correct in (third, third*2):
        print "You need more practice"
    else:
        print "Well done" 
    start_again = raw_input("Do you want to star again(press q -- exit or y -- continue) ")
    if start_again.lower() == 'y':
        continue
    elif start_again.lower() == 'q':
        print "Exiting"
        break
        