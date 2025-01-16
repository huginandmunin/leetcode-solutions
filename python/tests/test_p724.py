from p724_find_pivot_index import Solution


def test_solution1():
    solution = Solution()
    nums = [1,7,3,6,5,6]
    expected = 3
    assert solution.pivotIndex(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [1,2,3]
    expected = -1
    assert solution.pivotIndex(nums)==expected

def test_solution3():
    solution = Solution()
    nums = [2,-1,1]
    expected = 0
    assert solution.pivotIndex(nums)==expected