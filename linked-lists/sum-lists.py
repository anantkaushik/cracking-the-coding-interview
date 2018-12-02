"""
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse
order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as
the linked list. 

Example:
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP:
Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
"""
def addTwoNumbers(l1, l2):
    res = ListNode(0)
    cur = res
    carry = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        summ = carry + x + y
        carry = summ // 10
        cur.next = ListNode(summ%10)
        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry > 0:
        cur.next = ListNode(carry)
    return res.next

""" Follow Up """
class Solution(object):
    def addTwoList(self, l1, l2):
        len1,len2 = self.getLength(l1),self.getLength(l2)
        if len1 > len2:
            l2 = self.addLeadingZeroes(len1-len2,l2)
        else:
            l1 = self.addLeadingZeroes(len2-len1,l1)
        carry, summ = self.addNumbers(l1,l2)
        if carry > 0:
            new = ListNode(carry)
            new.next = summ
            summ = new
        return summ
        
    def getLength(self, node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count
    
    def addLeadingZeroes(self,count,node):
        for i in range(count):
            new = ListNode(0)
            new.next = node
            node = new
        return node
    
    def addNumbers(self,l1,l2):
        if not l1 and not l2:
            return (0,None)
        carry,new = self.addNumbers(l1.next,l2.next)
        summ = l1.val + l2.val + carry
        ans = ListNode(summ%10)
        ans.next = new
        return (summ//10,ans)