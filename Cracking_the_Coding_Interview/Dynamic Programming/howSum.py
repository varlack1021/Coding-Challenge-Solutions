def howSum(targetSum, nums, memo={}):
	if targetSum in memo: return memo[targetSum]

	if targetSum == 0: return []

	if targetSum < 0: return None

	for num in nums:
		remainder = targetSum - num
		remainderResult = howSum(remainder, nums)
		
		if remainderResult != None:
			remainderResult.append(num)
			memo[targetSum] = remainderResult

			return remainderResult

	memo[targetSum] = remainderResult
	return None

#print(howSum(7, [2,4])) # [7]
#print(howSum(7, [5,3,4,7])) # [7]
#print(howSum(8, [1, 4, 5])) # [4, 4]
print(howSum(100, [7,14, 25])) # [25, 25, 25, 25]