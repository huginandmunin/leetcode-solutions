from p3174_clear_digits import Solution


def test_solution1():
    solution = Solution()
    s = "abc"
    expected = "abc"
    assert solution.clearDigits(s)==expected

def test_solution2():
    solution = Solution()
    s = "abc123"
    expected = ""
    assert solution.clearDigits(s)==expected
