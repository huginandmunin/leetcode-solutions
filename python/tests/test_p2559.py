from p2559_count_vowel_strings_in_ranges import Solution

def test_solution1():
    solution = Solution()
    words = ["aba","bcb","ece","aa","e"]
    queries = [[0,2],[1,4],[1,1]]
    expected = [2,3,0]
    assert solution.vowelStrings(words,queries)==expected

def test_solution2():
    solution = Solution()
    words = ["a","e","i"]
    queries = [[0,2],[0,1],[2,2]]
    expected = [3,2,1]
    assert solution.vowelStrings(words,queries)==expected