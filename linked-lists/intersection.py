"""
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.
Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
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
