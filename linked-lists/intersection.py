"""
Given two singly linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection
is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference)
as the jth node of the second linked list, then they are intersecting.
"""
def getIntersectionNode(headA, headB):
    if headA == None or headB == None:
        return None
    A_pointer = headA
    B_pointer = headB
    while A_pointer != B_pointer:
        A_pointer = headB if A_pointer == None else A_pointer.next
        B_pointer = headA if B_pointer == None else B_pointer.next
    return A_pointer
