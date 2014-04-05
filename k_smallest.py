#!/usr/bin/python
# Bubble Sort to find k largest from an array

__author__ = "Kevin Aloyius"
def k_smallest(array, k):

	for i in range(len(array)):
		for j in range(len(array)-1):

			if array[j] < array[j+1]:
				temp = array[j+1]
				array[j+1] = array[j]
				array[j] = temp
	print array[:k]


def main():
	x = [3,4,5,6,5,795,564,5]
	k_smallest(x,2)

if __name__ == "__main__":
	main()
