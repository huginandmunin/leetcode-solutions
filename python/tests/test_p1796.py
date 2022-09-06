from p1796_second_largest_digit_in_string import Solution

def test_solution1():
    solution = Solution()
    s = "dfa12321afd"
    expected = 2
    assert solution.secondHighest(s)==expected

def test_solution2():
    solution = Solution()
    s = "abc1111"
    expected = -1
    assert solution.secondHighest(s)==expected

def test_solution3():
    solution = Solution()
    s = ""
    expected = -1
    assert solution.secondHighest(s)==expected

def test_solution4():
    solution = Solution()
    s = "aaa"
    expected = -1
    assert solution.secondHighest(s)==expected

def test_solution5():
    solution = Solution()
    s = "aaa1"
    expected = -1
    assert solution.secondHighest(s)==expected