from p2485_find_the_pivot_integer import Solution

def test_solution1():
    solution = Solution()
    n = 8
    expected = 6
    assert solution.pivotInteger(n)==expected

def test_solution2():
    solution = Solution()
    n = 1
    expected = 1
    assert solution.pivotInteger(n)==expected

def test_solution3():
    solution = Solution()
    n = 4
    expected = -1
    assert solution.pivotInteger(n)==expected