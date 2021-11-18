import sys
sys.path.append("..")

from p202_happy_number import Solution


def test_solution1():
    solution = Solution()
    input = 19
    expected = True
    assert solution.isHappy(input)==expected

def test_solution2():
    solution = Solution()
    input = 2
    expected = False
    assert solution.isHappy(input)==expected

def test_solution3():
    solution = Solution()
    input = 7
    expected = True
    assert solution.isHappy(input)==expected

def test_solution4():
    solution = Solution()
    input = 9
    expected = False
    assert solution.isHappy(input)==expected

def test_solution5():
    solution = Solution()
    input = 10
    expected = True
    assert solution.isHappy(input)==expected

def test_solution6():
    solution = Solution()
    input = 134
    expected = False
    assert solution.isHappy(input)==expected