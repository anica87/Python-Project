sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))


word_lenghts_second_way = [len(word) for word in words if word != "the"]

''' Using a  list comprehension, create a new list called "new list", which contains only the positive numbers from the list, as integers 
'''

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print numbers
new_list = [int(item) for item in numbers if item > 0]
print new_list