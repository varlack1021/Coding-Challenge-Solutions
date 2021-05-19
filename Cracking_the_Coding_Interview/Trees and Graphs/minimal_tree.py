'''
Give a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height. 
'''
class Node(object):
	"""docstring for Node"""
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def inOrderTraversal(self, node):
		'''
		if node.left:
			node = self.inOrderTraversal(node.left)
			print(node.val)
			return None

		print(node.val)
		
		if node.right:
			node = self.inOrderTraversal(node.right)
			print(node.val)
			return None
		'''
		if node is None:
			return

		print(node.val)
		node.inOrderTraversal(node.left)
		node.inOrderTraversal(node.right)
		
	def list_depths(self, node):
		'''
		each depth will  be a list
		'''
		lis = [[node]]
		vals = [[node.val]]

		while lis[-1] !=  []:
			lis.append([])
			vals.append([])

			for n in lis[-2]:
				if n.left:
					lis[-1].append(n.left)
					vals[-1].append(n.left.val)
				if n.right:
					lis[-1].append(n.right)
					vals[-1].append(n.right.val)
		
		return vals[:-1]

		
	def is_balanced(self, node):

		def getHeight(node):
			if node is None:
				return 0
			
			lheight = getHeight(node.left) + 1			
			rheight = getHeight(node.right) + 1
			
			if (lheight == -1 or rheight == -1): return -1
			if abs(lheight - rheight) > 1: return -1
			return max(lheight, rheight)

		if getHeight(node) > -1: return True
		return False

	def isBinarySearch(self, node):
		if node is None:
			return 

		mval = node.val
		if node.left:		
			lval = node.left.val

			if lval > mval:
				return False

		if node.right:
			rval = node.right.val

			if rval <  mval:
				return False
		
		m = self.isBinarySearch(node.left)
		n = self.isBinarySearch(node.right)
		print(m,n)
		if m in [False] or n in [False]:
			return False

		return True

def helper(lis):
	return minimal_tree(lis, 0, len(lis) - 1)

def minimal_tree(lis, start, end):
	if (end < start):
		return None

	mid = round((start + end) / 2)
	node = Node(lis[mid])
	node.left = minimal_tree(lis, start, mid-1)
	node.right = minimal_tree(lis, mid+1, end)
	return node



lis = [i for i in range(1,5)]
n  = helper(lis)

ans = n.list_depths(n)
#ans = n.is_balanced(n)
ans = n.isBinarySearch(n)
print(ans)