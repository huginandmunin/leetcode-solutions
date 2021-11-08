from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """ Split the tree into a left and right. 
            Recursively check the max depth of children. 
        """
        if root is None or (root.left is None and root.right is None):
            return True

        # Recusively check children
        depth = 0
        is_balanced = True
        depth,result = self.check_children(root, depth, is_balanced)
        return result


    def check_children(self, node: Optional[TreeNode],depth, is_balanced):
        # If we have a node then check for children
        diff = 0
        # is_balanced = True
        if node != None:
            depth += 1
            left_depth = 0
            right_depth = 0

            # Check number of children
            left_depth, is_balanced = self.check_children(node.left,depth, is_balanced)
            right_depth, is_balanced = self.check_children(node.right,depth, is_balanced)
            # Compare left and right
            if right_depth > left_depth:
                depth = right_depth
                diff = right_depth - left_depth
            else:
                depth = left_depth
                diff = left_depth - right_depth
            if diff > 1:
                is_balanced = False
        
        # Return when we run out nodes
        return depth, is_balanced

