#Given two sets (arrays) return their union

def union(list1,list2):

	union = []
	for element in list1:
		if not element in union:
			union.append(element)
	for element in list2:
		if not element in union:
			union.append(element)
	return union


def main():

	list1 = [1,2,3,65,79]
	list2 = [56,21,2,65,79]
	print union(list1,list2)
if __name__ == '__main__':
	main()