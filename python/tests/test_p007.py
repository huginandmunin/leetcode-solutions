import sys
sys.path.append("..")

from p007_reverse_integer import Solution


def test_solution1():
    solution = Solution()
    input = 123
    expected = 321
    assert solution.reverse(input)==expected

def test_solution2():
    solution = Solution()
    input = -123
    expected = -321
    assert solution.reverse(input)==expected

def test_solution3():
    solution = Solution()
    input = 120
    expected = 21
    assert solution.reverse(input)==expected

def test_solution4():
    solution = Solution()
    input = 0
    expected = 0
    assert solution.reverse(input)==expected
