from p2342_max_sum_of_a_pair_with_equal_sum_of_digits import Solution

def test_solution1():
    solution = Solution()
    nums = [18,43,36,13,7]
    expected = 54
    assert solution.maximumSum(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [10,12,19,14]
    expected = -1
    assert solution.maximumSum(nums)==expected