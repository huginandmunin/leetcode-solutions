from p3042_count_prefix_and_suffix_pairs_i import Solution

def test_solution1():
    solution = Solution()
    words = ["a","aba","ababa","aa"]
    expected = 4
    assert solution.countPrefixSuffixPairs(words)==expected

def test_solution2():
    solution = Solution()
    words = ["pa","papa","ma","mama"]
    expected = 2
    assert solution.countPrefixSuffixPairs(words)==expected

def test_solution3():
    solution = Solution()
    words = ["abab", "ab"]
    expected = 0
    assert solution.countPrefixSuffixPairs(words)==expected