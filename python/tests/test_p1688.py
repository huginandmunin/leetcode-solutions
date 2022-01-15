from p1688_count_of_matches_in_tournament import Solution

def test_solution1():
    solution = Solution()
    n = 7
    expected = 6
    assert solution.numberOfMatches(n)==expected

def test_solution2():
    solution = Solution()
    n = 14
    expected = 13
    assert solution.numberOfMatches(n)==expected