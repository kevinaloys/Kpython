#coding: utf-8
# Common courses
# A teacher wants to compare the performance of two students. To understand them better, he’s looking at all the other courses they took, but it’s hard to spot the common courses just from a glance.
# Given two arrays that contain the course IDs of two different students
# Your task is to
# write a function that prints to standard output (stdout) all the course IDs that are contained in both arrays, sorted in ascending order, one per line
# Note that your function will receive the following arguments:
# courses1
# which is the list of course IDs for the first student
# courses2
# which is the list of course ids for the second student
# Data constraints
# the length of the array given as input will not exceed 1000 elements
# Example
# Input	Output
# courses1: 1, 2, 8, 4, 5, 8, 3
# courses2: 8, 2, 2, 7, 10
# 2
# 8


def common_course(array1,array2):
	common = []
	for i in range(len(array1)):
		if(array1[i] in array2):
			common.append(array1[i])

	print "The Common coures are ", common

a = [235,245,245,452,654,600,498,541,654,542]
b = [654,452,452,600,564,5,48,498,145,612,653]
common_course(a,b)


