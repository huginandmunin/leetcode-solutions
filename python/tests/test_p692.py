from p692_top_k_frequent_words import Solution


def test_solution1():
    solution = Solution()
    words = ["i","love","leetcode","i","love","coding"]
    k = 2
    expected = ["i","love"]
    assert solution.topKFrequent(words,k)==expected

def test_solution2():
    solution = Solution()
    words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
    k = 4
    expected = ["the","is","sunny","day"]
    assert solution.topKFrequent(words,k)==expected

def test_solution3():
    solution = Solution()
    words = ["all", "work", "and", "no", "play", "makes", "jack", "a", "dull", "boy"]
    k = 10
    expected = ["a", "all", "and", "boy", "dull", "jack", "makes", "no", "play", "work"]
    assert solution.topKFrequent(words,k)==expected