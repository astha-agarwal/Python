# This program counts the number of vowels in  a text

# Author: Astha Agarwal
# Date: 21 june, 2015
# Version: 1.0

text = raw_input('Enter any text: ')

if text == '':
	print 'ERROR: No word entered'
else:
	#count stores the number of vowels in the text
	count_total_vowels = 0
	count_a = 0
	count_e = 0
	count_i = 0
	count_o = 0
	count_u = 0

	for letter in text:
		if letter == 'a':
			count_a += 1
			count_total_vowels += 1
		elif letter == 'e':
			count_e += 1
			count_total_vowels += 1
		elif letter == 'i':
			count_i += 1
			count_total_vowels += 1
		elif letter == 'o':
			count_o += 1
			count_total_vowels += 1
		elif letter == 'u':
			count_u += 1
			count_total_vowels += 1	

	print 'Total number of vowels in the text is: ',count_total_vowels
	print 'Total number of "a" is: ', count_a
	print 'Total number of "e" is: ', count_e
	print 'Total number of "i" is: ', count_i
	print 'Total number of "o" is: ', count_o
	print 'Total number of "u" is: ', count_u

	