from p3105_longest_strictly_increasing_or_strictly_decreasing_subarray import Solution


def test_solution1():
    solution = Solution()
    nums = [1,4,3,3,2]
    expected = 2
    assert solution.longestMonotonicSubarray(nums)==expected


def test_solution2():
    solution = Solution()
    nums = [3,3,3,3]
    expected = 1
    assert solution.longestMonotonicSubarray(nums)==expected


def test_solution3():
    solution = Solution()
    nums = [3,2,1]
    expected = 3
    assert solution.longestMonotonicSubarray(nums)==expected