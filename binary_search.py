#Implementing Binary Search. The Input is a sorted Array

__author__ = 'Kevin Aloysius'



def binary_search(list,key,start,end):
	mid = (start + end)/2
	if not key in list:
		print "The Key you are looking for is not available"
	elif (key == list[mid]):
		return mid
	elif (key < list[mid]):
		return binary_search(list,key,start,mid)
	elif (key > list[mid]):
		return binary_search(list,key,mid+1,end)
def main():
	x = [12,16,17,19,45,95,103]
	key = 17
	print "The Key",key,"is available at index",binary_search(x,key,0,len(x)-1)


if __name__ == '__main__':
	main()