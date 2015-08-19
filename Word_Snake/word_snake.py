'''
A word snake is (unsurprisingly) a snake made up of a sequence of words.
The program takes an input word sequence and turn it into a word snake. Here are the rules for the snake:
It has to start in the top left corner
Each word has to turn 90 degrees left or right to the previous word
The snake can't intersect itself
'''

# Author: Astha Agarwal
# Date: 22 july, 2015
# Version: 1.0

'''
The input will be a single line of words (written in ALL CAPS). 
The last letter of each word will be the first letter in the next.
'''

sequence = 'SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE'
list_words = sequence.split()

# print the first word
print list_words[0]
no_of_spaces = len(list_words[0])

# delete the word from the list 
list_words = list_words[1:]

# horizontal keeps track of how the word ids printed
horizontal = False

for word in list_words:

	if horizontal == True:
		print '\b' + word[1:]
		horizontal = False
		no_of_spaces += len(word) - 1

	else:
		word_length = len(word)
		for index in range(1,word_length):
			for space in range(no_of_spaces-1):
				print "",
			if index != word_length - 1:
				print word[index]
			else :
				print word[index],
		horizontal = True

