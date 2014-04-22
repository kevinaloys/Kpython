import os

__author__ = "Kevin Aloysius"
def list_dir(directory_location):
	print "Parent Directory +", directory_location
	print "Subdirectory:"
	for each_dirctorty in os.listdir(directory_location):
		print "-",each_dirctorty

list_dir('/dev')