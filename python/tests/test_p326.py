from p326_power_of_three import Solution


def test_solution1():
    solution = Solution()
    n = 27
    expected = True
    assert solution.isPowerOfThree(n)==expected

def test_solution2():
    solution = Solution()
    n = 0
    expected = False
    assert solution.isPowerOfThree(n)==expected

def test_solution3():
    solution = Solution()
    n = 1
    expected = True
    assert solution.isPowerOfThree(n)==expected

def test_solution4():
    solution = Solution()
    n = -1
    expected = False
    assert solution.isPowerOfThree(n)==expected