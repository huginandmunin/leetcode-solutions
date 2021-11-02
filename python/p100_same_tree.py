from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ Traverse each tree and see if values are same.
            Need to check node-by-node.
        """
        # Both trees are empty
        if (not p and not q):
            return True
        elif (p and not q) or (not p and q):
            return False
        # Check value of parent node then go through left and right children
        result = ((p and q) and (p.val == q.val ) and 
                self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        if not result:
            return False
        else:
            return True
