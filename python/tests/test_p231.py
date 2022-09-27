from p231_power_of_two import Solution


def test_solution1():
    solution = Solution()
    n = 1
    expected = True
    assert solution.isPowerOfTwo(n)==expected

def test_solution2():
    solution = Solution()
    n = 16
    expected = True
    assert solution.isPowerOfTwo(n)==expected

def test_solution3():
    solution = Solution()
    n = 3
    expected = False
    assert solution.isPowerOfTwo(n)==expected