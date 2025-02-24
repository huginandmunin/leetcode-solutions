from p1910_remove_all_occurrences_of_a_substring import Solution


def test_solution1():
    solution = Solution()
    s = "daabcbaabcbc"
    part = "abc"
    expected="dab"
    assert solution.removeOccurrences(s, part)==expected

def test_solution2():
    solution = Solution()
    s = "axxxxyyyyb"
    part = "xy"
    expected="ab"
    assert solution.removeOccurrences(s, part)==expected