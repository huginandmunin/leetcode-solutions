from p342_power_of_four import Solution


def test_solution1():
    solution = Solution()
    n = 16
    expected = True
    assert solution.isPowerOfFour(n)==expected

def test_solution2():
    solution = Solution()
    n = 5
    expected = False
    assert solution.isPowerOfFour(n)==expected

def test_solution3():
    solution = Solution()
    n = 1
    expected = True
    assert solution.isPowerOfFour(n)==expected