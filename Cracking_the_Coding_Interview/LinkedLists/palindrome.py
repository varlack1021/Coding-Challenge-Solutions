import time
from linkedlist import node, linkedList
lis = ['a', 'n', 'u', 't', 'f', 'o','r', 'a','j', 'a', 'r', 'o', 'f', 't', 'u', 'n', 'a']
pal = []

head = node(data=lis[0])
link = head

#Puts the palindrome into a linked list
for x in range(1, len(lis)):
	new_node = node(data=lis[x])
	link.setNode(new_node)
	link = link.getNode()


#I add it to a list and then iterate the list
#
def palindrome(head):
	while head.getNode():
		pal.append(head.getData())
		head = head.getNode()

	pal.append(head.getData())

	half = int(len(pal)/2)

	for x in range(half):
	
		if pal[x] != pal[len(pal) - x - 1]:
			return True
			
	 
if not palindrome(head):
	print("Palindrome")
else:
	print("Not Palindrome")

