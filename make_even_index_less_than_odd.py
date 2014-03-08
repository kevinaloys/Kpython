# Change an array, such that the indices of even numbers is less than that of odd numbers,
# Algorithnms Midterm 2 test question
def even_index(array):
	
	index = []
	for i in range(len(array)):

		if(array[i]%2==1):

			index.append(i) #Append the index of odd number to the end of the list 'index'

		else:

			index.insert(0,i)	#Append the index of even number at the beginning of the list 'index'
		
	
	for i in index:
		print array[i],		


a = [9,15,1,7,191,13,139,239,785,127,8786]

even_index(a)