# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        '''
        The idea is to subtract the value of the current node while dfs down the path
        pseudocode:

        if there isn't a root
            return false
        sum -= node.val
        if leaf node:
            check if sum == 0 return true if not return false
        recursively call the function on the left and right child
        '''
        if not root:
            return False
        
        targetSum -= root.val
        
        if not root.left and not root.right:
            #leaf
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        
       
            
        
        