def bestSum(targetSum, nums, memo={}):
	if targetSum == 0: 
		return []

	if targetSum < 0: return None

	shortestCombination = None

	for num in nums:
		remainder = targetSum - num
		remainderCombination = bestSum(remainder, nums)
		
		if remainderCombination != None:
			remainderCombination.append(num)

			if shortestCombination == None or len(remainderCombination) < len(shortestCombination):
				shortestCombination = remainderCombination

			if len(remainderCombination) > len(shortestCombination):
				return shortestCombination

	return shortestCombination

#print(bestSum(7, [2,4])) # None
#print(bestSum(7, [5,3,4,7])) # [7]
#print(bestSum(8, [1, 4, 5])) # [4, 4]
print(bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]