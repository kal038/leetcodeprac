# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = None
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
 
        def recurse(node):
            
            if not node:
                return False
            
            left = recurse(node.left)
            right = recurse(node.right)
            
            mid = (node == p or node == q)
            
            if mid + left + right >=2:
                self.ans = node
                
            return  mid or left or right
        
        recurse(root)
        
        return self.ans