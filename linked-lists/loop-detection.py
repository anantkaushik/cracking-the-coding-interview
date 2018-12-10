"""
Given a circular linked list, implement an algorithm that return the node at the begining of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a 
loop in the linked list.

Example:
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
"""
def detectCycle(head):
    slow = fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast == None or fast.next == None:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast