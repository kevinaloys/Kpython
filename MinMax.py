#
#
# To find minimum and maximum in an array
#
__author__="Kevin Aloysius"
def minmax(a):

	max = a[0]
	min = a[0]
	for i in range(1,len(a)):
		if(a[i]>max):
			max = a[i]
		elif(a[i]<min):
			min = a[i]
	print "Min ",min
	print "Max", max




a=[59,8,4,5,65,4,5,5,4,5,6,21,2,6,5,48,786,5,45,4,11,1]
minmax(a)