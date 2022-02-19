# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
[3,9,20,null,null,15,7]
2 
'''
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
        if root node is None
            return 1
        if root node is not none
            1 + min(minDepth(root.left), minDepth(root.right))
        
        '''
        if not root:
            return 0
        if (root.left == None):
            return self.minDepth(root.right) + 1
        if (root.right == None):
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1