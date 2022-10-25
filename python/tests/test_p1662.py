from p1662_check_if_two_strings_are_equivalent import Solution

def test_solution1():
    solution = Solution()
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    expected = True
    assert solution.arrayStringsAreEqual(word1,word2)==expected

def test_solution2():
    solution = Solution()
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    expected = False
    assert solution.arrayStringsAreEqual(word1,word2)==expected

def test_solution3():
    solution = Solution()
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    expected = True
    assert solution.arrayStringsAreEqual(word1,word2)==expected