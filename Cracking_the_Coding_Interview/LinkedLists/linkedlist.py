import time
class node(object):

	def __init__(self, node=None, data=None):
		self.node = node
		self.data = data

	def getData(self):
		return self.data

	def setNode(self, node=None):
		self.node = node

	def getNode(self):
		return self.node


##Creates a linked list with a size equal to the value of the input data
class linkedList(object):

	def __init__(self, data=None, head=None):
		self.data = data
		self.head = head
	
		for x in range(self.head.getData()+ 1, data):
		
			head = self.head
			
			while head.getNode():
				head = head.getNode()
			
			new_node = node(data=x)
			head.setNode(new_node)
		
	def print_list(self):
		head = self.head
		while head.getNode():
			print(head.getData())
			head = head.getNode()
		print(head.getData())
	def delete_node(self, data):
		prev_node = self.head
		curr_node = self.head.getNode() 

		if self.head.getData() == data:
			self.head = self.head.getNode()
		
		while curr_node.getNode():
				
			if(curr_node.getData() == data):

				next_node = curr_node.getNode()	
				prev_node.setNode(next_node)
				curr_node.setNode(None)
				return
				
			prev_node = prev_node.getNode()
			curr_node = curr_node.getNode() 
		print("Did not find any nodes to delete")

	def insert_node(self, node, loc):

		if loc == 0:
			node.setNode(self.head)
			self.head = node
			return

		insert = loc + 1
		head = self.head
		while insert != loc and not head.getNode():
			###add a and statement and fix inser loop
			head = head.getNode()
		next_node = head.getNode()
		node.setNode(next_node)
		head.setNode(node)

	def next(self):
		return self.head.getNode()

	def data(self):
		return self.head.getData()

	def get_Head(self):
		return self.head


#head = node(data=10)
#lis = linkedList(5, head)
#lis.print_list()

#lis.delete_node(data=45)

#new_node = node(data=15)

#lis.insert_node(new_node, 2)
#lis.print_list()

	
##add remove a node with a certain value
##add add a node to
##length of a list


#Python calling multiple methods on an object
	
	


