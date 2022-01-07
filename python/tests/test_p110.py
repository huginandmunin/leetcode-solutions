from p110_balanced_binary_tree import Solution, TreeNode

def test_solution1():
    # input = [1]
    solution = Solution()
    input_tree = TreeNode(1)
    expected = True
    assert solution.isBalanced(input_tree)==expected

def test_solution2():
    # input = []
    solution = Solution()
    input_tree = None
    expected = True
    assert solution.isBalanced(input_tree)==expected

def test_solution3():
    # input = [1,2]
    #   1
    #  /
    # 2
    solution = Solution()
    input_tree = TreeNode(1)
    input_tree.left = TreeNode(2)
    expected = True
    assert solution.isBalanced(input_tree)==expected

def test_solution4():
    # input = [1,None,2]
    #  1
    #   \
    #    2
    solution = Solution()
    input_tree = TreeNode(1)
    input_tree.right = TreeNode(2)
    expected = True
    assert solution.isBalanced(input_tree)==expected

def test_solution5():
    # input = [1,None,2,3]
    #  1
    #   \
    #    2
    #   /
    #  3
    solution = Solution()
    input_tree = TreeNode(1)
    input_tree.right = TreeNode(2)
    input_tree.right.left = TreeNode(3)
    expected = False
    assert solution.isBalanced(input_tree)==expected

def test_solution6():
    # input = [1,2,None,3]
    #  1
    #   \
    #    2
    #   /
    #  3
    solution = Solution()
    input_tree = TreeNode(1)
    input_tree.left = TreeNode(2)
    input_tree.left.left = TreeNode(3)
    expected = False
    assert solution.isBalanced(input_tree)==expected
 
def test_solution7():
    # input = [3,9,20,null,null,15,7]')
    #    3
    #   / \
    #  9   20
    #     /  \
    #    15   7
    solution = Solution()
    input_tree = TreeNode(3)
    input_tree.left = TreeNode(9)
    input_tree.right = TreeNode(20)
    input_tree.right.left = TreeNode(15)
    input_tree.right.right = TreeNode(7)    
    expected = True
    assert solution.isBalanced(input_tree)==expected

def test_solution8():
    # input = [1,2,2,3,3,None,None,4,4]
    #       1
    #      / \
    #     2   2
    #    / \ 
    #   3   3 
    #  / \
    # 4   4
    solution = Solution()
    input_tree = TreeNode(1)
    input_tree.left = TreeNode(2)
    input_tree.right = TreeNode(2)
    input_tree.left.left = TreeNode(3)
    input_tree.left.right = TreeNode(3)
    input_tree.left.left.left = TreeNode(4)
    input_tree.left.left.right = TreeNode(4)
    expected = False
    assert solution.isBalanced(input_tree)==expected

def test_solution9():
    # input [0,2,4,1,null,3,-1,5,1,null,6,null,8]
    #        0
    #       / \
    #      2   4
    #     /   / \
    #    1   3  -1
    #   / \   \   \
    #  5   1   6   8
    solution = Solution()
    input_tree = TreeNode(0)
    input_tree.left = TreeNode(2)
    input_tree.right = TreeNode(4)
    input_tree.left.left = TreeNode(1)
    input_tree.right.left = TreeNode(3)
    input_tree.right.right = TreeNode(-1)
    input_tree.left.left.left = TreeNode(5)
    input_tree.left.left.right = TreeNode(1)
    input_tree.right.left.right = TreeNode(6)
    input_tree.right.right.right = TreeNode(8)
    expected = False
    assert solution.isBalanced(input_tree)==expected