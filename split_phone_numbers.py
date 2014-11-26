import re

def split_phone(string):

	pattern = re.compile('([\d]{1,3})[\s|-]([\d]{1,3})[\s|-]([\d]{4,10})')
	match = re.match(pattern, string)
	print('CountryCode='+match.group(1)+',LocalAreaCode='+match.group(2)+',Number='+match.group(3))

def main():
	number = int(input())
	input_string = []
	for i in range(number):
		input_string.append(input())

	for each_string in input_string:
		split_phone(each_string)

if __name__ =='__main__':
	main()