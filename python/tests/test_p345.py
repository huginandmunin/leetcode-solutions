from p345_reverse_vowels_of_a_string import Solution

def test_solution1():
    solution = Solution()
    s = "IceCreAm"
    expected =  "AceCreIm"
    assert solution.reverseVowels(s)==expected

def test_solution2():
    solution = Solution()
    s = "leetcode"
    expected = "leotcede"
    assert solution.reverseVowels(s)==expected

def test_solution3():
    solution = Solution()
    s = ".,"
    expected = ".,"
    assert solution.reverseVowels(s)==expected