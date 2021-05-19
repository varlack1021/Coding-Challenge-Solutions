'''
[3, 6, 2, 9, -1, 10]
left

arr: [1, 4, 100, 5]
right


arr: [1, 10, 5, 1, 0, 6]
""

Given a binary tree in the form of an array, write a function that determines 
whetherr tthe left or right tree is bigger by the sum of the nodes
If the tree has equal nodes or there are 0 nodes, return the empty string

'''

import math
def left_or_right(arr):

	n = math.floor(math.sqrt(len(arr)))
	lsum = 0
	tsum = 0

	for i in range(1, n+1):
		start = (2**i )  - 1
		stop =  (2**(i-1)) + start
		
		if stop > len(arr):
			for x in arr[start:]:
				if x !=  -1:
					lsum += x
		else:
			for x in arr[start:stop]:
				if x != -1:
					lsum += x
	
	for x in arr[1:]:
		if  x != -1:
			tsum += x

	if tsum - lsum > lsum:
		return 'right'

	if tsum - lsum < lsum:
		return 'left'
	
	return 'equal'

a = [3, 6, 2, 9, -1, 10]
print(left_or_right(a))

a = [1, 4, 100, 5]
print(left_or_right(a))

a = [1, 10, 5, 1, 0, 6]
print(left_or_right(a))