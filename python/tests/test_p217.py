from p217_contains_duplicate import Solution


def test_solution1():
    solution = Solution()
    nums = [1,2,3,1]
    expected = True
    assert solution.containsDuplicate(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [1,2,3,4]
    expected = False
    assert solution.containsDuplicate(nums)==expected

def test_solution3():
    solution = Solution()
    nums = [1,1,1,11,2,3,4]
    expected = True
    assert solution.containsDuplicate(nums)==expected