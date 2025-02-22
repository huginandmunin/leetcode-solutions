from p041_first_missing_positive import Solution


def test_solution1():
    solution = Solution()
    nums = [1,2,0]
    expected = 3
    assert solution.firstMissingPositive(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [3,4,-1,1]
    expected = 2
    assert solution.firstMissingPositive(nums)==expected

def test_solution3():
    solution = Solution()
    nums = [7,8,9,11,12]
    expected = 1
    assert solution.firstMissingPositive(nums)==expected

def test_solution4():
    solution = Solution()
    nums = [100000, 3, 4000, 2, 15, 1, 99999]
    expected = 4
    assert solution.firstMissingPositive(nums)==expected