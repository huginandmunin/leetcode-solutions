from p080_remove_duplicates_from_sorted_array_II import Solution


def test_solution1():
    solution = Solution()
    nums = [1]
    expected = 1
    assert solution.removeDuplicates(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [1,1]
    expected = 2
    assert solution.removeDuplicates(nums)==expected

def test_solution3():
    solution = Solution()
    nums = [1,2]
    expected = 2
    assert solution.removeDuplicates(nums)==expected

def test_solution4():
    solution = Solution()
    nums = [1,1,2]
    expected = 3
    assert solution.removeDuplicates(nums)==expected

def test_solution5():
    solution = Solution()
    nums = [1,1,1,1,2]
    expected = 3
    assert solution.removeDuplicates(nums)==expected

def test_solution6():
    solution = Solution()
    nums = [1,1,1,2,2,3]
    expected = 5
    assert solution.removeDuplicates(nums)==expected

def test_solution7():
    solution = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    expected = 7
    assert solution.removeDuplicates(nums)==expected
