'''
Created on Jul 30, 2014

@author: anicam
'''
import random


if __name__ == '__main__':
    pass

s_nouns = ["A dude", " A mom "]
p_nouns = ["These dudes", "BOth of my moms"]
s_verbs= ["eats", "kicks"]
p_verbs =["eat", "kick"]
infinitives =["to make a pie", "for no apparent reasion"]



if raw_input("Wolud you like to add a new word? ").lower() =="yes":
    new_word = raw_input("Please enter a singular noun.")
    s_nouns.append(new_word)
    print s_nouns
    
else:
    print random.choice(s_nouns), random.choice(p_nouns), random.choice(s_nouns).lower() 