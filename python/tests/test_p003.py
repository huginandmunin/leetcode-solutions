from p003_longest_substring_without_repeating import Solution


def test_solution1():
    solution = Solution()
    input = 'abcabcbb'
    expected = 3
    assert solution.lengthOfLongestSubstring(input)==expected

def test_solution2():
    solution = Solution()
    input = 'bbbbb'
    expected = 1
    assert solution.lengthOfLongestSubstring(input)==expected

def test_solution3():
    solution = Solution()
    input = 'pwwkew'
    expected = 3
    assert solution.lengthOfLongestSubstring(input)==expected

def test_solution4():
    solution = Solution()
    input = 'aab'
    expected = 2
    assert solution.lengthOfLongestSubstring(input)==expected

def test_solution5():
    solution = Solution()
    input = 'aaabcaabcdef'
    expected = 6
    assert solution.lengthOfLongestSubstring(input)==expected