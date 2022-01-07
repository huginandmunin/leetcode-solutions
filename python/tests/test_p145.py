from p145_binary_tree_postorder_traversal import Solution, TreeNode

def test_solution1():
    # input = [1]
    solution = Solution()
    input_tree = TreeNode(1)
    expected = [1]
    assert solution.postorderTraversal(input_tree)==expected

def test_solution2():
    # input = []
    solution = Solution()
    input_tree = None
    expected = []
    assert solution.postorderTraversal(input_tree)==expected

def test_solution3():
    # input = [1,2]
    #   1
    #  /
    # 2
    solution = Solution()
    input_tree = TreeNode(1)
    input_tree.left = TreeNode(2)
    expected = [2,1]
    assert solution.postorderTraversal(input_tree)==expected

def test_solution4():
    # input = [1,None,2]
    #  1
    #   \
    #    2
    solution = Solution()
    input_tree = TreeNode(1)
    input_tree.right = TreeNode(2)
    expected = [2,1]
    assert solution.postorderTraversal(input_tree)==expected

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
    expected = [3,2,1]
    assert solution.postorderTraversal(input_tree)==expected
