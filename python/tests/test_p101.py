import sys
sys.path.append("..")

from p101_symmetric_tree import Solution, TreeNode

def test_solution1():
    # input = []
    solution = Solution()
    r = None
    expected = True
    assert solution.isSymmetric(r)==expected

def test_solution2():
    # input = [0]
    solution = Solution()
    r = TreeNode(0)
    expected = True
    assert solution.isSymmetric(r)==expected

def test_solution3():
    # input = [0,1,1,2,None,None,2]
    #     0
    #    / \
    #   1   1
    #  /     \
    # 2       2
    solution = Solution()
    r = TreeNode(0)
    r.left = TreeNode(1)
    r.left.left = TreeNode(2)
    r.right = TreeNode(1)
    r.right.right = TreeNode(2)
    expected = True
    assert solution.isSymmetric(r)==expected

def test_solution4():
    # input = [1,2,2,3,4,4,3]
    #      1
    #     / \
    #    /   \
    #   2     2
    #  / \   / \
    # 3   4 4   3
    solution = Solution()
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(2)
    r.left.left = TreeNode(3)
    r.left.right = TreeNode(4)
    r.right.left = TreeNode(4)
    r.right.right = TreeNode(3)
    expected = True
    assert solution.isSymmetric(r)==expected

def test_solution5():
    # input = [1,2,2,None,3,None,3]
    #     1
    #    / \
    #   2   2
    #    \   \
    #     3   3
    solution = Solution()
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(2)
    r.left.right = TreeNode(3)
    r.right.right = TreeNode(3)
    expected = False
    assert solution.isSymmetric(r)==expected

def test_solution6():
    # input = [1,2,2,None,3,3,None]
    #      1
    #     / \
    #    /   \
    #   2     2
    #    \   /
    #     3 3
    solution = Solution()
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(2)
    r.left.right = TreeNode(3)
    r.right.left = TreeNode(3)
    expected = True
    assert solution.isSymmetric(r)==expected