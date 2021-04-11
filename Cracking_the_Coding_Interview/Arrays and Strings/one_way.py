'''
There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if they are 
one edit (or zero edits) away.

Two Pointer Solution
'''
def insert(s1,  s2):
	diffs = 0
	j = 0
	
	for i in range(len(s2)):

		if s1[i+j] != s2[i]:
			diffs += 1
			j+= 1
			if diffs > 1:
				return False

	return True

def one_away(s1, s2):
	if s1 == s2:
		return True

	if abs(len(s1) - len(s2)) > 1:
		return False

	diff = 0

	if len(s1) == len(s2):
		insert(s1, s2)
	
	if len(s1) > len(s2):
		return insert(s1, s2)
	if len(s2) > len(s1):
		return insert(s2, s1)

	return True


s1 = 'pale'
s2 = 'pale'
print(one_away(s1, s2))

s1 = 'pale'
s2 = 'patient'
print(one_away(s1, s2))


s1 = ''
s2 = 'patient'
print(one_away(s1, s2))

s1 = 'pale'
s2 = ''
print(one_away(s1, s2))

s1 = 'pale'
s2 = 'ple'
print(one_away(s1, s2))

s1 = 'pale'
s2 = 'pla'
print(one_away(s1, s2))

s1 = 'pale'
s2 = 'pal'
print(one_away(s1, s2))