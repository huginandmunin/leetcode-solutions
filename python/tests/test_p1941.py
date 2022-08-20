from p1941_check_if_all_characters_have_equal_number_of_occurrences import Solution


def test_solution1():
    solution = Solution()
    s = "abacbc"
    expected = True
    assert solution.areOccurrencesEqual(s)==expected

def test_solution2():
    solution = Solution()
    s = "aaabb"
    expected = False
    assert solution.areOccurrencesEqual(s)==expected
