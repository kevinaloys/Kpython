# Sorting students

# After an exam all the students are graded and sorted by their grades.

# In some cases, students talk to the professor and conclude that one of the tougher problem statements in the exam was unclear and the teacher decides to remove its contribution towards the final grade.

# Since it’s just one of many challenges, the sorted list of students won’t change much - only a few students might change their order.

# How do we implement an efficient algorithm that sorts a list of numbers that are almost sorted? Bubble sort is the perfect one for this specific case:

#     bubblesort(A):
#     repeat
#         changed = false
#         for i = 1 to length(A) - 1
#             if A[i - 1] > A[i]
#                 swap A[i - 1], A[i]
#                 changed = true
#     until not changed
  

# Given an array of integer numbers

# Your task is to

#     implement the bubblesort algorithm to sort the array in ascending order and print the sorted elements to standard output (stdout), one per line

# Note that your function will receive the following arguments:

#     numbers
#         which is the array of integer numbers that needs to be sorted

# Data constraints

#     the length of the array given as input will not exceed 1000 elements

# Example
# Input 	Output

# numbers: 1, 9, 4, 5, 7
	

# 1 4 5 7 9

def bubble_sort(array):

	for i in range(len(array)-1):

		if(array[i]>array[i+1]):
			temp = array[i+1]
			array[i+1] = array[i]
			array[i] = temp

	print array

a = [1,9,4,5,7]
bubble_sort(a)