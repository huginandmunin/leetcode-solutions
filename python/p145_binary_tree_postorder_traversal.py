from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        vals = self.postorder(root,vals)
        return vals


    def postorder(self, root: Optional[TreeNode],vals):
        if root != None:
            self.postorder(root.left,vals)
            self.postorder(root.right,vals)
            vals.append(root.val)
        return vals