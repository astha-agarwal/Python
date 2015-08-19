# This program counts the number of words in  a text file

# Author: Astha Agarwal
# Date: 21 june, 2015
# Version: 1.0

file_name = 'read.txt'
file_object = open(file_name)

# initializes the number of words in the file to 0
word_count = 0

# the first character  in the file is read in 'char'
char = file_object.read(1) 

# run the loop until end of file is reached
while (char != ''):
	char = file_object.read(1) 

	# if there is a space after the character the word count is increased by 1
	if char == ' ':
		word_count += 1

	# if there is a new line character again the word count is increased by 1
	elif char == '\n':
		word_count += 1

# print an empty line and the result
print 
print 'The number of words in file', file_name, 'is', word_count
print
file_object.close()
