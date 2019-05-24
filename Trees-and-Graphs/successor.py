"""
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. 
You may assume that each node has link to its parent.
"""
def inOrderSuccessor(n): 
	if not n:
	    return None
	if n.right is not None: 
		return leftMostChild(n.right) 
	q = n
	x = q.parent
	while x != None and x.left != q:
	    q = x
	    x = x.parent
	return x

def leftMostChild(node): 
    if not node:
        return None    
    while node.left:
        node = node.left 
    return node
