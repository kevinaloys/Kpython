import re
def has_hackerrank(string):
	pattern = re.compile('hackerrank',re.IGNORECASE)
	if pattern.search(string):
		return(True)
	else:
		return(False)

def main():
	number = int(input())
	input_string = []
	for i in range(number):
		input_string.append(str(input()))
	count = 0
	for each_string in input_string:
		if has_hackerrank(each_string):
			count = count + 1
	print(count)


if __name__ == '__main__':
	main()