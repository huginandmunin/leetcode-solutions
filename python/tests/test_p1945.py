from p1945_sum_of_digits_of_string_after_convert import Solution


def test_solution1():
    solution = Solution()
    s = "iiii"
    k = 1
    expected = 36
    assert solution.getLucky(s,k)==expected

def test_solution2():
    solution = Solution()
    s = "leetcode"
    k = 2
    expected = 6
    assert solution.getLucky(s,k)==expected

def test_solution3():
    solution = Solution()
    s = "zbax"
    k = 2
    expected = 8
    assert solution.getLucky(s,k)==expected
