from p2185_counting_words_with_a_given_prefix import Solution

def test_solution1():
    solution = Solution()
    words = ["pay","attention","practice","attend"]
    prefix = "at"
    expected = 2
    assert solution.prefixCount(words, prefix)==expected

def test_solution2():
    solution = Solution()
    words = ["leetcode","win","loops","success"]
    prefix = "code"
    expected = 0
    assert solution.prefixCount(words, prefix)==expected