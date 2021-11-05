from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        vals = self.inorder(root,vals)
        return vals


    def inorder(self, root: Optional[TreeNode],vals):
        if root != None:
            self.inorder(root.left,vals)
            vals.append(root.val)
            self.inorder(root.right,vals)
        return vals

