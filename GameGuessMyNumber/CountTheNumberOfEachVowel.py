'''
Created on Dec 30, 2014

@author: anicam

Program to count the number of each vowel in a string
'''

vowels = 'aeiou'

user_input = raw_input('Enter a string: ')

# user_input = user_input.casefold()
# make it suitable for caseless compareisions
# dictionary comprehension
count = {}.fromkeys(vowels, 0)

for char in user_input:
    if char in count:
        count[char] += 1

print count

# for i in range(len(user_input)):
#     for j in range(len(vowel)):
#         if user_input[i] == vowel [j]:
#             count[j] += 1
# #             result.append(i)
# print count
  


# third way using comprehension dictionary, but this program is slower as we iterate over the entire input string for each vowel

result = { x: sum([ 1 for char in user_input if char == x]) for x in 'aeiou'}
print result
        