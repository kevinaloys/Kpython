#!/usr/bin/python
def k_largest(list, k):

	sorted_list = sorted(list)
	print sorted_list[-k:]

def main():
	x = [56,51,5,798,4,62,1,6]
	k_largest(x, 3)

if __name__ == "__main__":
	main()