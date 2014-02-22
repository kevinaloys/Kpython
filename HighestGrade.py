# Highest grade

# Given an array with all final grades for a course

# Your task is to

#     write a function that finds the highest grade and prints this grade to standard output (stdout)

# Note that your function will receive the following arguments:

#     grades
#         which is the list of grades, represented as integer numbers

# Data constraints

#     the length of the array given as input will not exceed 1000 elements

# Example
# Input 	Output

# grades: 1, 2, 8, 4, 5, 8, 3
	

# 8

def max_grade(a):

	max = a[0]
	for i in range(1,len(a)):
		if(a[i]>max):
			max = a[i]
		else:
			pass

	print max
		



a=[45,62,65,6,5,546548,48,7,8,8,9878]
max_grade(a)