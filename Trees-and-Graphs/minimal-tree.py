"""
Given a sorted(increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height.
"""
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def createMinimalBST(nums):
    if not nums:
        return None
    mid = (len(nums)-1)//2
    root = TreeNode(nums[mid])
    root.left = createMinimalBST(nums[:mid])
    root.right = createMinimalBST(nums[mid+1:])
    return root