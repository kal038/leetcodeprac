Pseudocode/Approach:
For this problem, it is easier to go for a recursive approach since it is a tree traversal problem and checking for equivalence along the way
We have a recursive function to spot if the two roots, if it is the root of the subtree as well, go on and check if they are the same tree
def isSame(root, subRoot):
check if both is null
return True
check if one of them is null
return False
return root.val == subRoot.val and isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
def isSubtree(root, subroot):
check if subRoot:
return True
check if root:
return False
return isSame(root, subRoot) or isSubtree(root.left, subRoot)  or isSubtree(root.right, subRoot)