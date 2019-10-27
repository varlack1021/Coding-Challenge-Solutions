from linkedlist import linkedList
from linkedlist import node
head = linkedlist(5)

for x in range (5):
	new_node = node(5, 1)
	head.insert(new_node)
head.print_list()

'''
Two ways to solve:
	Brute force way:
		Iterate through list n^2 times and compare each element to the rest of the list

	Efficient:
		Create a buffer that stores values as you iterate through the list
'''

buffers = []
while head.getData():
	data = head.getData()
	
	if data in buffers:
		head.delete(data)

	head = head.getNode()

