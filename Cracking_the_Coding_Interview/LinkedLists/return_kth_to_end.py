'''
Solution: Traverses to the end and 
counts backwards
'''


from linkedlist import linkedList, node

entry= node(data=1)
lis = linkedList(10, entry)
lis.print_list()

def return_kth_last(head, n):
	count = 0
	head = head
	adj = head.getNode()
	if head.getNode():
		count = 0 + return_kth_last(adj,n)

	print("the value of count is %d"  % (count))

	if count == n:
		print("data to be removed")
		print(head.getData())

	print(head.getData())
	##Would delete the nth node here
	return 1 + count

entry = lis.get_Head()   
return_kth_last(head=entry, n=10)
