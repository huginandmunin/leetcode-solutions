from p013_roman_to_integer import Solution


def test_solution1():
    solution = Solution()
    input = "III"
    expected = 3
    assert solution.romanToInt(input)==expected

def test_solution2():
    solution = Solution()
    input = "IV"
    expected = 4
    assert solution.romanToInt(input)==expected

def test_solution3():
    solution = Solution()
    input = "IX"
    expected = 9
    assert solution.romanToInt(input)==expected

def test_solution4():
    solution = Solution()
    input = "LVIII"
    expected = 58
    assert solution.romanToInt(input)==expected

def test_solution5():
    solution = Solution()
    input = "MCMXCIV"
    expected = 1994
    assert solution.romanToInt(input)==expected

def test_solution6():
    solution = Solution()
    input = "D"
    expected = 500
    assert solution.romanToInt(input)==expected
