'''
There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if they are 
one edit (or zero edits) away.

Two Pointer Solution
'''

def one_away(s1, s2):
	if s1 == s2:
		return True

	if len(s1) - len(s2) > 1:
		return False

	diffs = 0
	l = max(len(s1), len(s2))

	for i in range(l):
		if s1[i] != s2[i]:
			

	return True if diffs > 1 else False

s1 = pale
s2 = ple