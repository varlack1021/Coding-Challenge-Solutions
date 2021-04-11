'''
Implement an algorithm to determine if a string has all unique characters. What if you 
cannot use additional data structures?
'''

def is_unique(s):
	s = list(s)
	s.sort()
	count = len(s)
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			count -= 1
	return count

string = 'abc'
print(is_unique(string))

string = 'abbc'
print(is_unique(string))

string = 'abbbbbbbbc'
print(is_unique(string))

string = 'abbbbbbbbcbbbbbbbb'
print(is_unique(string))

string = 'abbbbbbbbcbbbbjklbbbbn'
print(is_unique(string))