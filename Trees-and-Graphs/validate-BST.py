"""
Implement a function to check if a binary tree is a binary search tree.
"""
def isBST(root,minn = float('-inf'), maxx=float('inf')):
    if not root:
        return True
    if root.data <= minn or root.data > maxx:
        return False
    if not isBST(root.left,minn,root.data):
        return False
    if not isBST(root.right,root.data,maxx):
        return False
    return True