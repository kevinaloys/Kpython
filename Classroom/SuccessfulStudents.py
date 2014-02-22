# Successful students

# Given an array with all final grades for a course and the minimum grade that a student needs to have in order to pass the course

# Your task is to

#     write a function that counts the number of students that passed and prints this number to standard output (stdout)

# Note that your function will receive the following arguments:

#     grades
#         which is the list of grades, represented as integer numbers
#     min_grade
#         which is the minimum grade that a student can get, so that he passes the course

# Data constraints

#     the length of the array given as input will not exceed 1000 elements

# Example
# Input 	Output

# grades: 1, 2, 8, 4, 5, 8, 3
# min_grade: 5
	

# 3

# Explanation

#     There were 3 students that passed the course - those with the grades: 8, 5, 8.



def count_successful_studens(grades, min_grade):

	passed = 0

	for i in range(len(grades)):
		if (grades[i] >= min_grade):
			passed += 1

	print "Successful Students", passed

grades = [1,2,8,4,5,8,3,5,68,5,4,65,1,2,65,7,85,6,5,7,86,5,4,23,54,6,87,5,65,4]
min_grade = 6
count_successful_studens(grades, min_grade)