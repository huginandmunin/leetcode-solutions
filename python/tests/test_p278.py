from p278_first_bad_version import Solution

def test_solution1():
    solution = Solution()
    n = 5
    # bad = 4
    expected = 4
    assert solution.firstBadVersion(n)==expected