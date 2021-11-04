from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """ Split the tree into a left and right. 
            Recursively check that opposite children match
            using a manner similar to P100 - Same Tree. 
        """
        if root is None or (root.left is None and root.right is None):
            return True

        if root.left is None or root.right is None:
            return False

        # Recusively check children
        result = self.are_mirror_trees(root.left, root.right)
        return result


    def are_mirror_trees(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ Traverse each tree inorder and see if values are mirrored. """

        # Both trees are empty
        if (not p and not q):
            return True
        elif (p and not q) or (not p and q):
            return False
        # Check value of parent node then go through left and right children
        result = ((p and q) and (p.val == q.val ) and 
                self.are_mirror_trees(p.left, q.right) and self.are_mirror_trees(p.right, q.left))
        if not result:
            return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()

    r = None
    print(f'\ninput = []')
    result = solution.isSymmetric(r)
    print(f'output = {result}')

    r = TreeNode(0)
    print(f'\ninput = [0]')
    result = solution.isSymmetric(r)
    print(f'output = {result}')

    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(2)
    r.left.left = TreeNode(3)
    r.left.right = TreeNode(4)
    r.right.left = TreeNode(4)
    r.right.right = TreeNode(3)
    print(f'\ninput = [1,2,2,3,4,4,3]')
    result = solution.isSymmetric(r)
    print(f'output = {result}')

    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(2)
    r.left.right = TreeNode(3)
    r.right.right = TreeNode(3)
    print(f'\ninput = [1,2,2,null,3,null,3]')
    result = solution.isSymmetric(r)
    print(f'output = {result}')