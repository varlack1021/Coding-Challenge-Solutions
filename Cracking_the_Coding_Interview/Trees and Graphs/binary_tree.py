class Node(object):
	"""docstring for Node"""
	def __init__(self, val=None, link=None):
		self.link = link
		self.val = val
		

class BinaryTree():

	def __init__(self, val=None, left=None, right=None):
		self.left = left
		self.right = right
