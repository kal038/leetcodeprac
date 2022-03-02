# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
        :type root: TreeNode
        :rtype: bool
        
        
        We do a DFS recursion to reach the leaf of the tree and use a helper function to identify symmetry
        
        Pseudocode:
        if root is null return true
        else:
            return check symmetry(root.left, root.right)
            
        check_symmetry:
        
        if not a and not b:
            return True
        if not a or not b:
            return False
        else:
            return a.data == b.data and check_symm(a.left, b.right) and check_symm(a.right, b.left)
            
        Time: O(n)
        Space: O(h)
'''
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        else:
            return self.check_symmetry(root.left, root.right)
        
        
    def check_symmetry(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        else:
            return a.val == b.val and self.check_symmetry(a.left, b.right) and self.check_symmetry(a.right, b.left)
        