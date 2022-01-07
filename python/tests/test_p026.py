from p026_remove_duplicates_from_sorted_array import Solution


def test_solution1():
    solution = Solution()
    input = [1,1,2]
    expected = 2
    assert solution.removeDuplicates(input)==expected

def test_solution2():
    solution = Solution()
    input = [0,0,1,1,1,2,2,3,3,4]
    expected = 5
    assert solution.removeDuplicates(input)==expected

def test_solution3():
    solution = Solution()
    input = [1,2,2,3]
    expected = 3
    assert solution.removeDuplicates(input)==expected