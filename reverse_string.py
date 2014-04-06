# Define a function reverse() that computes the reversal of a string. For
# example, reverse("I am testing") should return the string "gnitset ma I".

__author__ = "Kevin Aloysius"

def reverse_string(string):

	string_list = list(string)
	string_list = string[::-1]
	string = ''.join(string_list)
	return string

def main():
	x = "I am testing"
	print reverse_string(x)

if __name__ == "__main__":
	main()