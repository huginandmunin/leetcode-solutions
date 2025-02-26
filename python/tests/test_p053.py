from p053_maximum_subarray import Solution

def test_solution1():
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    expected = 6
    assert solution.maxSubArray(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [1]
    expected = 1
    assert solution.maxSubArray(nums)==expected

def test_solution3():
    solution = Solution()
    nums = [5,4,-1,7,8]
    expected = 23
    assert solution.maxSubArray(nums)==expected