"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""
def NthFromEnd(self, head, n):
    p1,p2 = head,head
    if not head:
        return head
    for i in range(n):
        p1 = p1.next
    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2