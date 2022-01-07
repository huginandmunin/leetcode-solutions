from p258_add_digits import Solution


def test_solution1():
    solution = Solution()
    num = 38
    expected = 2
    assert solution.addDigits(num)==expected


def test_solution2():
    solution = Solution()
    num = 0
    expected = 0
    assert solution.addDigits(num)==expected


def test_solution3():
    solution = Solution()
    num = 11111
    expected = 5
    assert solution.addDigits(num)==expected