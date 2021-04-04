"""
Question:
Once you pay the cost, you can either climb one or two steps. 
You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Solution:
We know that the min cost to climb stairs would cost[i] = min(i-1, 1-2)
Therefore if we keep track of the min cost to reach each stair, we can solve this using Dynamic Programming

We will be using an array to represent the min cost to climb each stair at each index
Then we will compute the cost[i] by finding the min of the cost of the previous stairs + the min cost it took to get to that staircase (recorded in the array)

We will start at index 2 since the min cost to reach index 1 or 0 is 0
Ex: [10, 15, 20]

Initial array
dp =[0 0 0 0]

dp[2] = min(cost[1] + dp[1], cost[0] + dp[0]) = min(15 + 0, 10 + 0)
dp = [0, 0, 10, 0]

cost[3] (this is the goal) = min(cost[2] + dp[2], cost[1] + dp[1]) = min(20 + 10, 15 + 0)
dp = [0, 0, 10, 15]

The answer is the last cost in the dp array
"""
class Solution:
	def minCostToClimbStairs(self, cost):
		dp = [0] * len(cost)
		for i in range(2, len(cost) + 1)
			dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
		return dp[-1]