#This is a python program to generate bigram probablity of a sentence

def open_file(filename):
	f = open(filename,'rU')
	filenames = f.readlines()
	sentence = []

	for string in filenames:
		string = string.lower()
		string = string.strip()
		sentence.append(string)
	return sentence
		

def main():
	open_file('sample_text.txt')

if __name__ == "__main__":
	main()