#!/usr/bin/python
# Bubble Sort to find k largest from an array

__author__ = "Kevin Aloyius"
def k_smallest(array, k):
	for j in range(len(array)):
		for i in range(len(array)-j-1):
				if array[i] > array[i+1]:
					# temp = array[j+1]
					# array[j+1] = array[j]
					# array[j] = temp
					array[i], array[i+1] = array[i+1],array[i]

				print array


def main():
	x = [9,8,7,6,5,4,3,2,1]
	k_smallest(x,3)

if __name__ == "__main__":
	main()
