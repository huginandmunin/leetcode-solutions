from p916_word_subsets import Solution


def test_solution1():
    solution = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]
    expected = ["facebook","google","leetcode"]
    assert solution.wordSubsets(words1,words2)==expected


def test_solution2():
    solution = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["l","e"]
    expected = ["apple","google","leetcode"]
    assert solution.wordSubsets(words1,words2)==expected


def test_solution3():
    solution = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","oo"]
    expected = ["facebook","google"]
    assert solution.wordSubsets(words1,words2)==expected


def test_solution4():
    solution = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["lo","eo"]
    expected = ["google","leetcode"]
    assert solution.wordSubsets(words1,words2)==expected


def test_solution5():
    solution = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["ec","oc","ceo"]
    expected = ["facebook","leetcode"]
    assert solution.wordSubsets(words1,words2)==expected