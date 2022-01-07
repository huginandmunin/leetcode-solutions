from p100_same_tree import Solution, TreeNode

def test_solution1():
    # input = [1,2,3],[1,2,3]
    #   1       1
    #  / \     / \
    # 2   3   2   3
    solution = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    expected = True
    assert solution.isSameTree(p,q)==expected

def test_solution2():
    # input = [1,2],[1,None,2]
    #   1   1
    #  /     \
    # 2       2
    solution = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)
    expected = False
    assert solution.isSameTree(p,q)==expected

def test_solution3():
    # input = [1,2,1],[1,1,2]
    #   1       1
    #  / \     / \
    # 2   1   1   2
    solution = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    expected = False
    assert solution.isSameTree(p,q)==expected