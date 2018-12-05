"""
Implement a function to check if a linked list is a palindrome.
"""
class Solution(object):
    def isPalindrome(self, head):
        n = self.length(head)
        if n <= 1:
            return True
        firstHalfRev, secondHalf = self.rev(head,int(n/2))
        if n % 2 != 0:
            secondHalf = secondHalf.next
        while secondHalf:
            if secondHalf.val != firstHalfRev.val:
                return False
            secondHalf = secondHalf.next
            firstHalfRev = firstHalfRev.next
        return True
    
    def rev(self, node, l):
        newHead = None
        for i in range(l):
            if newHead is None:
                newHead = node
                node = node.next
                newHead.next = None
            else:
                tmp = node
                node = node.next
                tmp.next = newHead
                newHead = tmp
        return newHead,node
        
    def length(self, head):
        count = 0
        while (head):
            count = count + 1
            head = head.next
        return count