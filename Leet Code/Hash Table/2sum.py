'''
--------Problem---------

Find any two numbers in the list that add up to the target number
Assume there is only one unique solution
Return the indexes
--------Solution-------
Naive: N^2 iterate through the lists and add up all the values. If any of the values equal the target return those numbers

Optimal: Use a dictionary or hashmap to keep track of numbers we are looking for which results in a O N solution
For each number in the lis we will subtract it from the target. If the difference is in the dic then we return that number and the difference. 
If it is not in the dic then we add it to the dic

'''
def twoSum(target, lis):

	difference = {}
	for i in range(len(lis)):
		if target - lis[i] in difference:
			return [difference[target-lis[i]], i]
		else:
			difference[lis[i]] = i

