from p1446_consecutive_characters import Solution


def test_solution1():
    solution = Solution()
    s = "leetcode"
    expected = 2
    assert solution.maxPower(s)==expected

def test_solution2():
    solution = Solution()
    s = "abbcccddddeeeeedcba"
    expected = 5
    assert solution.maxPower(s)==expected

def test_solution3():
    solution = Solution()
    s = "cc"
    expected = 2
    assert solution.maxPower(s)==expected