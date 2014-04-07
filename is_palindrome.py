# Define a function is_palindrome() that recognizes palindromes (i.e. words that
# look the same written backwards). For example, is_palindrome("radar") should
# return True.

__author__ = "Kevin Aloysius"

def is_palindrome(string):
	result = True
	for i in range(len(string)/2):
		if string[i] != string[len(string)-1- i]:
			result = False
	return result


def main():
	string = "radar"
	print is_palindrome(string)

if __name__ == "__main__":
	main()