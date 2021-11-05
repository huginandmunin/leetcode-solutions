from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # Else recusively check number of children
        max_depth = 0
        max_depth = self.check_children(root,max_depth)
        return max_depth


    def check_children(self, root: Optional[TreeNode],max_depth):
        # If we have a node then check for children
        if root != None:
            max_depth += 1
            left_d = 0
            right_d = 0

            # Check number of children
            left_d = self.check_children(root.left,max_depth)
            right_d = self.check_children(root.right,max_depth)
            # Compare left and right
            if right_d > left_d:
                max_depth = right_d
            else:
                max_depth = left_d

        # Return when we run out nodes
        return max_depth
