#Write a function to check whether a given string contains duplicate words.
def duplicate_words(string):
	string_list = string.split()
	string_set = set(string_list)
	print string_list
	print string_set
	if len(string_list) == len(string_set):
		return False
	else:
		return True
print duplicate_words("hi i am kevin kevin")