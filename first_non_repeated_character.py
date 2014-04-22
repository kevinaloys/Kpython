# Find the First non-repeated character in a string.
def find_first_non_repeated_stirng(string):
	string = string + ' '
	first = string[0]
	for i in range(1,len(string)-1):
		if (string[i] != first):
			first = string[i]
			if string[i+1] != first:
				print "The First Non Repeating Character is '"+first+"'"
				break
def main():
	find_first_non_repeated_stirng('aaabbbcccgffff')

if __name__ == '__main__':
	main()