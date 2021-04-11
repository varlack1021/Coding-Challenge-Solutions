'''
Given two strings, write a method to decide if one is a permutation of the 
other. 
'''

def is_permutation(s1, s2):
	s1 = list(s1)
	s2 = list(s2)

	s1.sort()
	s2.sort()

	if s1 == s2:
		return True

	return False

s1 = "abcdefg"
s2 = "abdcgfe"

print(is_permutation(s1, s2))

s1 = "abcdefg"
s2 = " "

print(is_permutation(s1, s2))


s1 = "abcdefg"
s2 = "asdwcas "

print(is_permutation(s1, s2))