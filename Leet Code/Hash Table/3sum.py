'''
Given an array of integers, Find all cases where any 3 digits add up to zero, 
No repeating answers. [-1, 1, 0] == [1, 0, -1]
'''
#------------My Solution, Passed 311/313 test cases. Timed out but is N^2----------
def threeSum(nums):
    
    three_sum = []
    for i in range(len(nums)):
         
        target = 0 - nums[i]
        difference = {}
        
        for j in range(len(nums)):
            if j == i:
                continue
            
            if target - nums[j] in difference:

                sum_ = sorted([nums[i], target-nums[j], nums[j]])
                three_sum.add(sum_) if sum_ not in three_sum else None

            difference[nums[j]] = j
    print(three_sum)
    return list(three_sum)
print(threeSum([-1, 0, 1, 2, -1, -4]))

#---------------Solution that passed. Is also N^2--------------
def threeSum(self, nums: List[int]) -> List[List[int]]:
    sumOfThreeSet = set()
    lenOfNums = len(nums)
    nums = sorted(nums)
    for i in range(lenOfNums):
        j = i+1
        k = lenOfNums-1
        while (j < k):
            currentSum = nums[i] + nums[j] + nums[k]
            if currentSum == 0:
                sumOfThreeSet.add((nums[i], nums[j], nums[k]))
                j += 1
            else:
                if currentSum < 0:
                    #move the left pointer to increase the sum and bring it
                    # closer to zero
                    j += 1
                else:
                    #move the right pointer to decrease the sum and bring it closer
                    # to zero
                    k -= 1
    return list(sumOfThreeSet)