'''
Created on Dec 22, 2014

@author: anicam
'''

import re

print dir(re)

pattern = re.compile(r"\[(on|of)\]")
print re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]")
# Return  a Match object

print re.search(pattern, "Nada ... :-(")
# Doesn't return anything


def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print "Your failed to match %s" %(email)
        elif not your_pattern:
            print "Forgot to enter a pattern!"
        else:
            print "Pass"


pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"

'''
the caret ^ matches text at the beginning of a line
pipe | this is called the OR operator and the regex will match of the line start with any of the words in the group
The .*? means to un-greedily match any number of characters, expect the newline \n character
The un-greedy part means to match as few repetitions as possible.
The . character means any non-newline character.
the * menas to repeat 0 or more times
? character makes it un-greedy

'''