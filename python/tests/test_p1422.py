from p1422_maximum_score_after_splitting_a_string import Solution


def test_solution1():
    solution = Solution()
    s = "011101"
    expected = 5
    assert solution.maxScore(s)==expected

def test_solution2():
    solution = Solution()
    s = "00111"
    expected = 5
    assert solution.maxScore(s)==expected

def test_solution3():
    solution = Solution()
    s = "1111"
    expected = 3
    assert solution.maxScore(s)==expected

def test_solution4():
    solution = Solution()
    s = "11"
    expected = 1
    assert solution.maxScore(s)==expected