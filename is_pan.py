import re

def is_pan(string):
	pan = re.compile('[A-Z]{5}[0-9]{4}[A-Z]{1}')
	if pan.match(string):
		return True
	else:
		return False

def main():
	number = int(input())
	input_string = []
	for i in range(number):
		input_string.append(str(input()))

	for each_string in input_string:
		if is_pan(each_string):
			print('YES')
		else:
			print('NO')


if __name__ == '__main__':
	main()