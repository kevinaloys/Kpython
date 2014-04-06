# Write a function translate() that will translate a text into 
# (Swedish for "robber's language"). That is, double every consonant and place
# an occurrence of "o" in between. For example, translate("this is fun") should
# return the string "tothohisos isos fofunon".
__author__ = "Kevin Aloysius"
def robber_language(text):
	character_list = list(text)
	new_list = []
	for i in range(len(character_list)):
		if character_list[i] in 'aeiouAEIOU ':
			new_list.append(character_list[i])
		else:
			new_list.append(character_list[i]); new_list.append('o'); new_list.append(character_list[i])
	robber_text = ''.join(new_list)

	print robber_text

def main():
	text = "this is fun"
	robber_language(text)

if __name__ == "__main__":
	main()
