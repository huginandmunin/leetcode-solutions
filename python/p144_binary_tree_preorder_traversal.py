from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        vals = self.preorder(root,vals)
        return vals


    def preorder(self, root: Optional[TreeNode],vals):
        if root != None:
            vals.append(root.val)
            self.preorder(root.left,vals)
            self.preorder(root.right,vals)
        return vals