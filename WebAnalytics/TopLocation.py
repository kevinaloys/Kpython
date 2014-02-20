# Top locations

# Given three integer numbers a, b and c representing the number of unique visitors from three different locations

# Your task is to

#     write a function that prints to the standard output (stdout) the three values in ascending order (on the same line separated by a white space)

# Note that your function will receive the following arguments:

#     a
#         which is an integer representing the number of unique visitors from the first location
#     b
#         which is an integer representing the number of unique visitors from the second location
#     c
#         which is an integer representing the number of unique visitors from the third location

# Data constraints

#     the integer values will not exceed 1,000,000

# Example
# Input 	Output

# a: 1000
# b: 25
# c: 95
	

# 25 95 1000

# a: 100
# b: 125
# c: 95
	

# 95 100 125
__author__="Kevin Aloysius"

## Kevin Aloysius Quick and Dirty Method

def sort_location(a,b,c):
	x = list()			#Initilize a list x, Append the values of a,b and c to x, using the sort function to sort the values and priting them in a for loop
	x.append(a)
	x.append(b)
	x.append(c)

	x.sort()
	for i in x:
		print i

sort_location(1000,455,95)