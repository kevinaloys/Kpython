#This is a python program to calculate the bigram probablity of a sentence

def open_file(filename):
	f = open(filename,'rU')
	filenames = f.readlines()
	sentence = []

	for string in filenames:
		string = string.lower()
		string = string.strip()
		sentence.append(string)
	print sentence

def main():
	open_file('sample_text.txt')

if __name__ == "__main__":
	main()