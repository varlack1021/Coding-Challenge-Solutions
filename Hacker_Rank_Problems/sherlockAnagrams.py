def sherlockAndAnagrams(s):
	sub_strings = [s[x:y] for x, y in combinations(range( len(s) +1 ), r=2)]
	sorted_string = []	
	total = 0

	for string in sub_strings:
		letters = list(string)
		letters.sort()
		letters = "".join(letters)
		sorted_string.append(letters)

	sorted_string = Counter(sorted_string)

	for string in sorted_string:
		if sorted_string[string] > 1:
			n = sorted_string[string]

			while n > 1:
				total += n -1
				n -= 1