from p028_find_the_index_of_the_first_occurrence_in_a_string import Solution


def test_solution1():
    solution = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    expected = 0
    assert solution.strStr(haystack, needle)==expected

def test_solution2():
    solution = Solution()
    haystack = "leetcode"
    needle = "leeto"
    expected = -1
    assert solution.strStr(haystack, needle)==expected

def test_solution2():
    solution = Solution()
    haystack = "hello"
    needle = "ll"
    expected = 2
    assert solution.strStr(haystack, needle)==expected