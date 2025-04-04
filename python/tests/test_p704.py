from p704_binary_search import Solution

def test_solution1():
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    expected = 4
    assert solution.search(nums, target) == expected

def test_solution2():
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 2
    expected = -1
    assert solution.search(nums, target) == expected

