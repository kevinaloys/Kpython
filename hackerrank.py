import re


def main():
	number = int(input())
	input_string = []
	for i in range(number):
		input_string.append(str(input()))

	for each_string in input_string:
		if each_string.startswith('hackerrank') and each_string.endswith('hackerrank'):
			print('0')
		elif each_string.startswith('hackerrank'):
			print('1')
		elif each_string.endswith('hackerrank'):
			print('2')
		else:
			print('-1')

if __name__ == '__main__':
	main()