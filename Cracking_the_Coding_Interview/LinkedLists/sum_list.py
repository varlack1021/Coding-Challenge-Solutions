'''
My solution: Traverse to the end of the linked list
Then when returning up, add each node value to a string
Then return the string as an int and add both operads
Finally add the string to a linkedlist

Another solution - add the linked lists together recursively
'''

from linkedlist import linkedList, node

head1 = node(None, 1)
head2 = node(None, 1)
lis1 = linkedList(data=4, head=head1)
lis2 = linkedList(data=8, head=head2)

operand1 = ""
operand2 = ""

def convert_operand(head, operand):
	if head.getNode():
		operand = convert_operand(head.getNode(), operand)
	return  operand + str((head.getData()))
 
operand1 = int(convert_operand(head1, operand1))
operand2 = int(convert_operand(head2, operand2))

total = operand1 + operand2
total = str(total)

head = node(data=total[len(total) - 1])
link = head
print(total)
control = len(total) - 1

for x in range(control):
	data = total[control - x - 1]
	new_node = node(data=data)
	link.setNode(new_node)
	link = link.getNode()

while head.getNode():
	print(head.getData())
	head = head.getNode()
print(head.getData())

def add_linked_lists(head1, head2)


