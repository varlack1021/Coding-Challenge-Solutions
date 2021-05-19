'''
Assume you have a method isSubst ring which checks if one word is a substring 
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one 
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat")
'''

def string_rotation(s1, s2):
	if s2 in s1+s1:
		return True

s1 = 'waterbottle'
s2 = 'erbottlewat'

print(string_rotation(s1, s2))