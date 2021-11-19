import sys
sys.path.append("..")

from p509_fibonacci_number import Solution


def test_solution1():
    solution = Solution()
    input = 1
    expected = 1
    assert solution.fib(input)==expected

def test_solution2():
    solution = Solution()
    input = 2
    expected = 1
    assert solution.fib(input)==expected

def test_solution3():
    solution = Solution()
    input = 3
    expected = 2
    assert solution.fib(input)==expected

def test_solution4():
    solution = Solution()
    input = 5
    expected = 5
    assert solution.fib(input)==expected

def test_solution5():
    solution = Solution()
    input = 10
    expected = 55
    assert solution.fib(input)==expected