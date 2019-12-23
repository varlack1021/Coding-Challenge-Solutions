from collections import Counter
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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      
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


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not s or not wordDict:
            return False
        starting_index = 0
        stack = [starting_index]
        visited = set()
        while stack:
            starting_index = stack.pop()
            
            if starting_index in visited:
                continue
            visited.add(starting_index)
            for word in wordDict:
                
                if s[starting_index:].startswith(word):
                    x = len(word)                
                    if x == len(s[starting_index:]):
                        return True
                    stack.append(starting_index + x)
        return False

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = []
        y = []
        while l1.next != None:
            x.insert(0, str(l1.val))
            l1 = l1.next
        
        x.insert(0, str(l1.val))
        
        while l2.next != None:
            y.insert(0, str(l2.val))
            l2 = l2.next
        y.insert(0, str(l2.val))
        
        result = int("".join(x)) + int("".join(y))
        lis = [ x for x in str(result)]
        lis.reverse()
        
        
        head = n = ListNode(lis.pop(0))
        
        for data in lis:
            node = ListNode(data)
            n.next = node
            n = node
        
        
        
        print(result)
        return head
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            
            carry, output = divmod(val1 + val2 + carry, 10)
            
            tempNode = ListNode(output)
            node.next = tempNode
            node = tempNode
            
            l1 = (l1.next if l1 else 0)
            l2 = (l2.next if l2 else 0)
        return head.next