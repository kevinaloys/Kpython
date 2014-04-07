

# # Define a procedure histogram() that takes a list of integers and prints a
# # histogram to the screen. For example, histogram([4, 9, 7]) should print the
# # following:

# ****
# *********
# *******

__author__ = "Kevin Aloysius"

def histogram(list):

	for i in range(len(list)):
		star_printer(list[i])
		print "\n",


def star_printer(number):

	for i in range(number):
		print "*",

def main():

	number_list = [4,9,4,6,8,7]
	histogram(number_list)

if __name__ == "__main__":
	main()