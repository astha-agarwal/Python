'''A garland word is one that starts and ends with the same N letters in the same order,
 for some N greater than 0, but less than the length of the word. I'll call the maximum N 
 for which this works the garland word's degree. For instance, "onion" is a garland word 
 of degree 2, because its first 2 letters "on" are the same as its last 2 letters. 
 The name "garland word" comes from the fact that you can make chains of the word in this manner:

 onionionionionionionionionionion...

 This program, takes a lowercase word and returns the degree of the word if it's a garland word, 
 and 0 otherwise and then prints a chain of words'''


# Author: Astha Agarwal
# Date: 21 july, 2015
# Version: 1.0

def find_degree(word):
	degree = 0
	length = len(word)

	# In each iteration the starting 'index + 1' characters are compared to 
	# the last 'index + 1' characters
	for index in range(length-1):
		if word[0:index+1] == word[length-1-index:length]:
			degree = index + 1

	return degree

def garland(word, degree):
	# The word is repeated 10 times
	garland_word = ''
	for i in range(10):
		garland_word += word[degree:]
	return garland_word 	


print
word = raw_input('Enter any word: ')

if word == '':
	print 'Error: No word entered'
else:
	degree = find_degree(word)

print 'The degree of', word, 'is:', degree

# print out the garland word if degree is greater than 0
if degree > 0:
	print
	print word + garland(word, degree)
	print
else:
	print
	print 'It is not a garland word :('
	print





