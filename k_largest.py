# Finding the k largest number in an array
# This is the Bubble Sort Variation
# Will be posting selection sort variation soon..
def k_largest(k,array):

	for i in range(0,len(array)-1):

		for j in range(0,len(array)-1):
			if (array[j] < array[j+1]):
				temp = array[j+1]
				array[j+1] = array[j]
				array[j] = temp
	
	print "The",k,"largest numbers are"
	for i in range(k):
		print array[i]

a = [5,8,25,15,45,65,75,41,23]
k_largest(5,a)
