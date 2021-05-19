from linkedlist import linkedList, node

entry= node(data=1)
lis = linkedList(10, entry)
#lis.print_list()

def temp(head, n):
	if(head == None):
		return 0
	else:
		count = 1 + temp(head.getNode(), n)

		if count == n:
			print(head.getData())

		return count


entry = lis.get_Head()
temp(head=entry, n=5)