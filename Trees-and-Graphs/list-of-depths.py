"""
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
(eg: if you have a tree with Depth D, you'll have D linked lists).
"""
class node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = node()

	def append(self, data):
		new_node = node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node
        
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        
        current, res, level = [root], {}, 0
        
        while current:
            nex = []
            temp = LinkedList()
            for n in current:
                temp.append(n.val)
                if n.left:
                    nex.append(n.left)
                if n.right:
                    nex.append(n.right)
            current = nex
            res[level] = temp.head
            level += 1
        for i in res:
            self.display(res[i])
            print("")
        
    def display(self, head):
		cur = head
		while cur.next != None:
			cur = cur.next
			print(cur.data)