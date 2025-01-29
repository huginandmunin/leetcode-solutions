from p287_find_the_duplicate_number import Solution

def test_solution1():
    solution = Solution()
    nums = [1,3,4,2,2]
    expected = 2
    assert solution.findDuplicate(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [3,1,3,4,2]
    expected = 3
    assert solution.findDuplicate(nums)==expected

def test_solution3():
    solution = Solution()
    nums = [3,3,3,3,3]
    expected = 3
    assert solution.findDuplicate(nums)==expected