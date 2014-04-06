# Define a function sum() and a function multiply() that sums and multiplies
# (respectively) all the numbers in a list of numbers. For example, sum([1, 2,
# 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

__author__ = "Kevin Aloysius"

def sum(list):
	sum = 0
	for number in list:
		sum += number
	return sum

def multiply(list):
	product = 1
	for number in list:
		product *= number
	return product

def main():
	x=[1,2,3]
	print sum(x)
	print multiply(x)
if __name__ == "__main__":
	main()