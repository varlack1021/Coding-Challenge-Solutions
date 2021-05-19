def canSum(targetSum, nums, memo={}):
	if targetSum in memo: 
		return memo[targetSum]

	if targetSum == 0: return True

	if targetSum < 0: return False

	for num in nums:
		remainder = targetSum - num
		if canSum(remainder, nums, memo=memo):
			memo[targetSum] = True
			return True

	memo[targetSum] = False
	return False

#print(canSum(7, [2,4])) #false
#print(canSum(7, [5,3,4,7])) #true
#print(canSum(8, [2, 3, 5])) #true
#print(canSum(300, [7,14])) #false

def argTest(name={}):
	print(name)

argTest({'test':3})
argTest()