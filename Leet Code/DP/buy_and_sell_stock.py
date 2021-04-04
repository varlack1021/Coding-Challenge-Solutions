"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.


Solution:
O(N) solution

We iterate throught the list and keep track of the current minimum. With the minimum we subtract it from the next element in the list as we traverse.
If the curr_num - profit > curr_profit then we update curr profit. We only change the value of minimum if we find an element that is less than it. With
the new minimum we repeat the process of determing the profit until another min occurs or we reach the end of the list.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        if not prices:
            return 0
        
        buy = prices[0]
    
        for num in prices[1:]:
            
            if num - buy > profit:
                profit = num - buy
            
            if num < buy:
                buy = num
                
        return profit