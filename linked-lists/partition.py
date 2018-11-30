"""
Write a code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater 
than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x.
The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right
partitions. 

Example:
Input: head = 1->4->3->2->5->2, partition = 3
Output: 1->2->2->4->3->5
"""
def partition(head, x):
    headLess, headGreater = ListNode(0),ListNode(0)
    cur1, cur2 = headLess, headGreater
    
    while head:
        if head.val < x:
            cur1.next = head
            cur1 = cur1.next
        else:
            cur2.next = head
            cur2 = cur2.next
        head = head.next
    
    cur2.next = None
    cur1.next = headGreater.next
    return headLess.next