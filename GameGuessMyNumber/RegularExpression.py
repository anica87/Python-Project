'''
Created on Jan 5, 2015

@author: anicam
'''
from re import match
from test.test_profile import regenerate_expected_output

'''
Simple match
Find Spider-Man, Spiderman, SPIDER_MAN, etc.
'''
import re


dailybugle = 'SPIDER_MANx Menaces City'
pattern = r'spider[-,_ ]?man.'

if re.match(pattern, dailybugle, re.IGNORECASE):
    print dailybugle
    
'''
Match and capture group
Match dates formatted like MM/DD/YYYY , MM-DD-YY, ...
'''

date = '12/30/1969'
regex = re.compile(r'^(\d\d)[-/](\d\d)[/-](\d\d(?:\d\d)?)$')
match = regex.match(date)

if match:
    month = match.group(1)
    print month
    day = match.group(2)
    print day
    year = match.group(3)
    print year

'''
Simple substitution
Convert <br> to </br> for XHTML compliance
'''
text = 'Hello world. <br>'
regex = re.compile(r'<br>',re.IGNORECASE)
repl = r'<br />'

result = regex.sub(repl, text)
result_second_way = re.sub(regex, repl, text )
print text, result, result_second_way

'''
Harder substitution
turn URLs into HTML links
'''

text = 'Check the web site, http://www.oreilly.com/catalog/regexppr.'



pattern = r'''
\b # start at word boundary
( # capture to \1
( https?|telent|gopher|file|wais|ftp) :
# resource and colon
[\w/#~:.?+=$%@!\-] +? 
# one or more valid chars take a little as possible
)
(?= # lookahead
[.:?\-] * # for possible punc
(?: [^\w/#~:.?+=&%@!\-] # invalid character
| $ ) # or end of string
) '''
 
regex = re.compile(pattern, re.IGNORECASE + re.VERBOSE)

result = regex.sub(r'<a href = "\1">\1</a>', text)
print result

