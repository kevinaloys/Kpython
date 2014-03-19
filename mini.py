def minimum(array):
	min = array[0]
	for i in range(1,len(array)):

		if(array[i] < min):
			min = array[i]
		else:
			pass

	print min

array = [56,5,74,85,54,68,74,84,684,68,465,465,4]
minimum(array)

