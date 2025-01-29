from p268_missing_number import Solution

def test_solution1():
    solution = Solution()
    nums = [3,0,1]
    expected = 2
    assert solution.missingNumber(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [0,1]
    expected = 2
    assert solution.missingNumber(nums)==expected

def test_solution3():
    solution = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    expected = 8
    assert solution.missingNumber(nums)==expected

def test_solution4():
    solution = Solution()
    nums = [1,2,3,4]
    expected = 0
    assert solution.missingNumber(nums)==expected