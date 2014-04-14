#This is a python program to generate bigram probablity of a sentence

def open_file(filename):
	f = open(filename,'rU')
	filenames = f.readlines()
	if filenames == None:
		raise Excpetion("Nothing to read in file")
	sentence = []

	for string in filenames:
		string = string.lower() # Change string within the list into lower case for the sake of uniformity
		string = string.strip()	# Remove the trailing \n from the end of the sentence
		sentence.append(string)
	return sentence

def corpus_generation(sentence_list):
	corpus_list = []
	for sentence in sentence_list:
		strings = sentence.split(' ')
		for string in strings:
			corpus_list.append(string)

	return corpus_list
def main():

	sentence_list = open_file('sample_text.txt')
	print corpus_generation(sentence_list)

if __name__ == "__main__":
	main()