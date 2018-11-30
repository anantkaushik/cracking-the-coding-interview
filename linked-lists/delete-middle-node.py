"""
Implement an algorithm to delete a node in the middle (i.e. any node but the first and last node, 
not necessarily the exact middle) of a singly linked list, given only access to that node.
"""
def deleteNode(node):
    if node == None or node.next == None:
        return False
    node.val, node.next = node.next.val, node.next.next
    return True