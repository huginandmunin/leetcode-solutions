from p2965_find_missing_and_repeated_values import Solution

def test_solution1():
    solution = Solution()
    grid = [[1,3],[2,2]]
    expected = [2, 4]
    assert solution.findMissingAndRepeatedValues(grid)==expected

def test_solution2():
    solution = Solution()
    grid = [[9,1,7],[8,9,2],[3,4,6]]
    expected = [9, 5]
    assert solution.findMissingAndRepeatedValues(grid)==expected

def test_solution3():
    solution = Solution()
    grid = [[2,2],[3,4]]
    expected = [2, 1]
    assert solution.findMissingAndRepeatedValues(grid)==expected