"""
Write a code to remove duplicates from an unsorted linked list.
Follow Up:
How would you solve this problem if a temprorary buffer is not allowed?
"""
def deleteDuplicates(head):
    if not head:
        return head
    cur = head
    while cur:
        runner = cur
        while runner.next:
            if runner.next.val == cur.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next
    return head