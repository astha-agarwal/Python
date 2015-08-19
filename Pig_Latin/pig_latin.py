# The program takes in a word and converts it into pig Latin
# In pig Latin the initial consonant is transposed to the end of word and an 'ay' is affixed
# If the initial sound is a vowel then 'yay' is affixed at the end

# Author: Astha Agarwal
# Date: 21 july, 2015
# Version: 1.0

word = raw_input('Enter any word: ')

if word == '':
	print 'Error: No word entered'
else:
	word_pig_latin = ''
	length = len(word)

	#if word starts with a vowel
	if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':    
		word_pig_latin = word + 'yay'
	#if word starts with a consonant
	else:
		word_pig_latin = word[1:] + word[0] + 'ay'
	print word_pig_latin
