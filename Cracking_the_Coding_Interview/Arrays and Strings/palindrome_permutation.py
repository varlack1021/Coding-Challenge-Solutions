from collections import Counter

def  palindrome_permutation(s):
	s = s.split()
	s = "".join(s)
	count = Counter(s)

	num_odds = 0 
	print(count)
	for l, c in count.items():
		if c%2 != 0:
			num_odds+=1

	if num_odds > 1:
		return False
	return True

s = "tact coa"
print(palindrome_permutation(s))

s = "ttt aa b"
print(palindrome_permutation(s))

s = "tt dd vv ee"
print(palindrome_permutation(s))

s = ""
print(palindrome_permutation(s))

s = " "
print(palindrome_permutation(s))
