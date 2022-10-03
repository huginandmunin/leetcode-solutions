from p046_permutations import Solution

def test_solution1():
    solution = Solution()
    nums = [1,2,3]
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert solution.permute(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [0,1]
    expected = [[0,1],[1,0]]
    assert solution.permute(nums)==expected

def test_solution3():
    solution = Solution()
    nums = [1]
    expected = [[1]]
    assert solution.permute(nums)==expected