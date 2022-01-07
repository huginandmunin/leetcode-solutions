from p357_count_numbers_with_unique_digits import Solution


def test_solution1():
    solution = Solution()
    n = 0
    expected = 1
    assert solution.countNumbersWithUniqueDigits(n)==expected

def test_solution2():
    solution = Solution()
    n = 1
    expected = 10
    assert solution.countNumbersWithUniqueDigits(n)==expected

def test_solution3():
    solution = Solution()
    n = 2
    expected = 91
    assert solution.countNumbersWithUniqueDigits(n)==expected

def test_solution4():
    solution = Solution()
    n = 3
    expected = 739
    assert solution.countNumbersWithUniqueDigits(n)==expected