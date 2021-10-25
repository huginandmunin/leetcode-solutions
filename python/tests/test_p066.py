import sys
sys.path.append("..")

from p066_plus_one import Solution


def test_solution1():
    solution = Solution()
    input = [1,2,3]
    expected = [1,2,4]
    assert solution.plusOne(input)==expected

def test_solution2():
    solution = Solution()
    input = [4,3,2,1]
    expected = [4,3,2,2]
    assert solution.plusOne(input)==expected

def test_solution3():
    solution = Solution()
    input = [0]
    expected = [1]
    assert solution.plusOne(input)==expected

def test_solution4():
    solution = Solution()
    input = [9,9,9]
    expected = [1,0,0,0]
    assert solution.plusOne(input)==expected

def test_solution5():
    solution = Solution()
    input = [4,8,9,3,0,9]
    expected = [4,8,9,3,1,0]
    assert solution.plusOne(input)==expected

def test_solution5():
    solution = Solution()
    input = [4,8,9,3,0,9,3]
    expected = [4,8,9,3,0,9,4]
    assert solution.plusOne(input)==expected