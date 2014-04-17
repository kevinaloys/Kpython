#Given an unordered list of numbers find all pairs that add up to x


def find_all_pair(list,x):
	pair = []
	for i in range(len(list)-1):
		for j in range(i+1,len(list)):
			if list[i] + list[j] == x:
				if not [list[i],list[j]] in pair:
					pair.append([list[i], list[j]])
	print pair


def main():
	list = [5,1,6,48,5,54,65,6,9,4,5,6,984,2,13,24,6,5,86,635,463,54,687,56,413,54,654,6354,65,746,54,65,76,87654,5]
	find_all_pair(list,70)

if __name__ == '__main__':
	main()