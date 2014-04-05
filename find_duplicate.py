#!/usr/bin/python
# Find duplicate in a number
def find_duplicate(array):

	for i in range(1,len(array)):
		if array[i] == array[i-1]:
			print array[i]
		else:
			pass

def main():

	x = [1,2,3,3,4,4,5,5,6,6,7,8,9]
	find_duplicate(x)

if __name__ == "__main__":
	main()