from p557_reverse_words_in_a_string_iii import Solution


def test_solution1():
    solution = Solution()
    s = "Let's take LeetCode contest"
    expected = "s'teL ekat edoCteeL tsetnoc"
    assert solution.reverseWords(s)==expected

def test_solution2():
    solution = Solution()
    s = "God Ding"
    expected = "doG gniD"
    assert solution.reverseWords(s)==expected