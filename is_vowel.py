# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
#/usr/bin/python

__author__ = "Kevin Aloysius"

def is_vowel(char):

	return char.lower() in 'aeiou'

def main():
	print is_vowel('a')

if __name__ == "__main__":
	main()
