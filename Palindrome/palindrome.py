# This program checks if the string entered by the user is palindrome. 
# Thai is that it reads the same forwards as backwards, like racecar

# Author: Astha Agarwal
# Date: 21 june, 2015
# Version: 1.0

while(True):
	print ''
	print 'Press enter to exit...'
	word = raw_input('Enter a word to check for palindrome: ')

	if word == '':
		break
	else:
		length = len(word)
		output = True
		for index in range(length/2):
			if word[index] != word[length-1-index]:
				output = False
				break
		if output == True:
			print 'It is a palindrome!!'
		else:
			 print 'Not a palindrome'