#For this one I used a queue to keep track of the order 
#in which the nodes were added
#add a node to the queue then add its children to the end of the queue
#I then used a dummy data "\n" to insert into the queue to indicate
#a new level has started
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    queue = []
    level_order = []
    level_num = 0
    
    head = root
    if head:
        queue.append(head)
        queue.append("\n")
        level_order.append([])
    else:
        return level_order
    
    while queue != ["\n"]:
        node = queue.pop(0)
        
        if node == "\n":
            queue.append("\n")
            level_order.append([])
            level_num += 1
            continue
        
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
        
        level_order[level_num].append(node.val)
    
    return level_order