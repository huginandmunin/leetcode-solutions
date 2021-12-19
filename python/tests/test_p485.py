from p485_max_consecutive_ones import Solution

def test_solution1():
    solution = Solution()
    nums = [1,1,0,1,1,1]
    expected = 3
    assert solution.findMaxConsecutiveOnes(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [1,0,1,1,0,1]
    expected = 2
    assert solution.findMaxConsecutiveOnes(nums)==expected