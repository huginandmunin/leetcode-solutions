from p008_string_to_integer import Solution


def test_solution1():
    solution = Solution()
    input = "42"
    expected = 42
    assert solution.myAtoi(input)==expected

def test_solution2():
    solution = Solution()
    input = "  -42"
    expected = -42
    assert solution.myAtoi(input)==expected

def test_solution3():
    solution = Solution()
    input = "4193 with words"
    expected = 4193
    assert solution.myAtoi(input)==expected

def test_solution4():
    solution = Solution()
    input = f"{2 ** 31 + 5}"
    expected = 2 ** 31 - 1
    assert solution.myAtoi(input)==expected

def test_solution5():
    solution = Solution()
    input = "words and 987"
    expected = 0
    assert solution.myAtoi(input)==expected

def test_solution6():
    solution = Solution()
    input = ""
    expected = 0
    assert solution.myAtoi(input)==expected

def test_solution7():
    solution = Solution()
    input = " "
    expected = 0
    assert solution.myAtoi(input)==expected