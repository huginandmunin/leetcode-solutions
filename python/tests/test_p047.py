from p047_permutations_ii import Solution

def test_solution1():
    solution = Solution()
    nums = [1,1,2]
    expected = [[1,1,2],[1,2,1],[2,1,1]]
    assert solution.permuteUnique(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [1,2,3]
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert solution.permuteUnique(nums)==expected
