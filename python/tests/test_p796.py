from p796_rotate_string import Solution

def test_solution1():
    solution = Solution()
    s = "abcde"
    goal = "cdeab"
    expected = True
    assert solution.rotateString(s,goal)==expected

def test_solution2():
    solution = Solution()
    s = "abcde"
    goal = "abced"
    expected = False
    assert solution.rotateString(s,goal)==expected