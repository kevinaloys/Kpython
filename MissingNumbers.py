# Missing number

# Given an array containing all numbers from 1 to N with the exception of one print the missing number to the standard output.

# Example input:
# array: 5 4 1 2

# Example output:
# 3

# Note: This challenge was part of Microsoft interviews. The expected complexity is O(N).



__author__="Kevin Aloysius"

def find_missing_number(n,array):
	for i in range(1,n):
		if i not in array:
			print i





array1 = [1,2,3,4,5,6,8,9,10]
find_missing_number(10,array1)