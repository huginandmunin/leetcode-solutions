import sys
sys.path.append("..")

from p012_integer_to_roman import Solution


def test_solution1():
    solution = Solution()
    input = 3
    expected = "III"
    assert solution.intToRoman(input)==expected

def test_solution2():
    solution = Solution()
    input = 4
    expected = "IV"
    assert solution.intToRoman(input)==expected

def test_solution3():
    solution = Solution()
    input = 9
    expected = "IX"
    assert solution.intToRoman(input)==expected

def test_solution4():
    solution = Solution()
    input = 58
    expected = "LVIII"
    assert solution.intToRoman(input)==expected

def test_solution5():
    solution = Solution()
    input = 1994
    expected = "MCMXCIV"
    assert solution.intToRoman(input)==expected

def test_solution6():
    solution = Solution()
    input = 500
    expected = "D"
    assert solution.intToRoman(input)==expected
