from collections import Counter
from itertools import combinations

combos = combinations(range(10), 2)
for x , y in combos:
	print(x, y)
arr = [1, 3, 9, 9, 27, 81]


def count_triplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0
    
    for v in arr:
        if v in r3:
            count += r3[v]
        
        if v in r2:
            r3[v*r] += r2[v]
        
        r2[v*r] += 1
        print(r2)
        print(r3)
        print("_____")
def longestPalindrome(self, s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]
	
s = "bbaacd"
def isValid(s):
    s = Counter(s)
    st = []
    flag = 0
    compare = 0
    print(s)
    
    for x in s:
        st.append(s[x])
    st.sort()
    compare = []
    print(st)
    st = set(st)
    print(st)
    
    if flag >= 2:
        return "NO"
    return "YES"


isValid(s)
	
class Solution:
    def wordBreak(self, s, wordDict):
      
        if not s or not wordDict:
                return False

        stack = [0]
        visited = set()
        while stack:
            starting_index = stack.pop()
            
            if starting_index in visited:
                continue
            visited.add(starting_index)
            for word in wordDict:
                
                if s[starting_index::].startswith(word):
                    x = len(word)                
                    if x == len(s[starting_index:]):
                        return True
                    stack.append(x)
        return False


