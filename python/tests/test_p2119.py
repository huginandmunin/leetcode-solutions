from p2119_a_number_after_double_reversal import Solution

def test_solution1():
    solution = Solution()
    num = 0
    expected = True
    assert solution.isSameAfterReversals(num)==expected

def test_solution2():
    solution = Solution()
    num = 541
    expected = True
    assert solution.isSameAfterReversals(num)==expected

def test_solution3():
    solution = Solution()
    num = 1800
    expected = False
    assert solution.isSameAfterReversals(num)==expected