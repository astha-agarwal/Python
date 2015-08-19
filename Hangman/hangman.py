# Hanngman game: Player has limited number of guesses to correctly identify a word.

# Author: Astha Agarwal
# Date: 28 july, 2015
# Version: 1.0

import random

hangman = (
	'''
	  +---+
	  |   |
	      |
	      |
	      |
	      |
	=========
	''', 
	'''
	  +---+
	  |   |
	  O   |
	      |
	      |
	      |
	=========
	''', 
	'''
	  +---+
	  |   |
	  O   |
	  |   |
	      |
	      |
	=========
	''', 
	'''
	  +---+
	  |   |
	  O   |
	 /|   |
	      |
	      |
	=========
	''', 
	'''
	  +---+
	  |   |
	  O   |
	 /|\  |
	      |
	      |
	=========
	''', 
	'''
	  +---+
	  |   |
	  O   |
	 /|\  |
	 /    |
	      |
	=========
	''', 
	'''
	  +---+
	  |   |
	  O   |
	 /|\  |
	 / \  |
	      |
	=========
	'''
	)

word_list = ('ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow',
						'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama',
						'mole', 'monkey','moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit',
						'ram', 'rat', 'raven', 'rhino', 'salmon','seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan',
						'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'zebra')

max_wrong = len(hangman)-1
word = random.choice(word_list)
word = word.upper()
wrong = 0
used = []
player_guess = '-'  * len(word)

def get_player_guess():
	# gets the input from user which should be a single character
	guess = raw_input('\n\nEnter your guess: ')
	guess = guess.upper()

	while guess in used:
		print '\nYou have already guessed this letter.'
		guess = raw_input('\n\nEnter your guess: ')
		guess = guess.upper()

	used.append(guess)
	return guess

def check_guess(guess):
	# check whether the character is in the word
	global player_guess
	global wrong
	if guess in word:
		new = ''
		print '\nYes!', guess, 'is in word.'
		for i in range(len(word)):
			if guess == word[i]:
				new += guess
			else:
				new += player_guess[i]
		player_guess = new

	else:
		print '\nWrong!', guess, 'is not in word.'
		wrong += 1

def main_loop():

	print \
'''
 _   _   _ _   _   _  ____  _    _    __   _   _ 
| | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |
| |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| |
|  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |
| | | || | | || |\  | |_\ \| |  | || | | || |\  |
\_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/
'''

	print '\n\nGuess the word'
	print player_guess
	print

	while (wrong < max_wrong) and (word != player_guess):
		guess = get_player_guess()
		check_guess(guess)
		print hangman[wrong]
		print '\nYou have the following letters: ', used
		print '\n', player_guess

	if (wrong == max_wrong):
		print hangman[wrong]
		print '\nYou have been hanged.'
	else:
		print '\nYou have guessed it.'

	print '\nThe word is:', word

main_loop()

