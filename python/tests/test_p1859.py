from p1859_sorting_the_sentences import Solution


def test_solution1():
    solution = Solution()
    s = "is2 sentence4 This1 a3"
    expected = "This is a sentence"
    assert solution.sortSentence(s)==expected

def test_solution2():
    solution = Solution()
    s = "Myself2 Me1 I4 and3"
    expected = "Me Myself and I"
    assert solution.sortSentence(s)==expected
