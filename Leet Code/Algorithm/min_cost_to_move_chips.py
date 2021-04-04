"""
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.

Solution

After doing a couple of test cases, I noticed that the cost to move chips will either be zero or 1 no matter their position. If we need 
to move chips from even to odd or odd to even it will cost 1 where if we do even-even or odd-odd it will cost 0.

Therefore I thought that if we just count the total odds and evens and find the minimum between them, that will be the minimum cost to move chips.

"""

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens = len([num for num in position if num %2 == 0])
        odds = len(position) - evens
        
        return evens if odds >= evens else odds