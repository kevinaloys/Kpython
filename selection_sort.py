#!/usr/bin/python
# Implementation of Selection Sort

__author__ = "Kevin Aloysius"

def selection_sort(array):
	
	for i in range(0,len(array)):
		minimum = i

		for j in range(i+1,len(array)):
			if array[j] < array[minimum]:
				temp = array[minimum]
				array[minimum] = array[j]
				array[j] = temp
		print array
def main():
	x = [6,5,4,3,2,1]
	selection_sort(x) 

if __name__ == "__main__":
	main()