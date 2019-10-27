import string
import pprint
valid_words = ["FACED", "CABBAGE", "BAGGAGE"]
puzzles = ["ABCDEFG"]

word_dic = {"A": [], 
			"B": [],
			"C": [],
			"D": [],
			"E": [],
			"F": [],
			"G": [],
			"H": [], 
			"J": [],
			"K": [],
			"L": [],
			"M": [],
			"N": [],
			"O": [], "P": [], "Q": [], "R": [], "S": [], "T": [], "U": [], "V": [], "W": [], "X": [], "Y": [], "Z": []}



for letter in word_dic.keys():
	for word in valid_words:
		if letter in word:
			word_dic[letter].append(word)

print(word_dic)

def check_puzzle():
	pass


