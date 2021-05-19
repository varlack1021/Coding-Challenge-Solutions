memo = {}
class Solution:

    
    def uniquePaths(self, m: int, n: list) -> int:
        #treat it like a binary tree
        #up or left
        #the comma is important to uniquely identify items
        key = f"{n},{m}"
        
        if key in memo:
            return memo[key]

        if n == 1 and m == 1:
            return 1

        if m == 0 or n == 0:
            return 0
        
        up = self.uniquePaths(m-1, n)
        down = self.uniquePaths(m,n-1)

        memo[key] = up + down
        return memo[key]

s = Solution()
print(s.uniquePaths(23,12))