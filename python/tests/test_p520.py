from p520_detect_capital import Solution

def test_solution1():
    solution = Solution()
    word = "USA"
    expected = True
    assert solution.detectCapitalUse(word)==expected

def test_solution2():
    solution = Solution()
    word = "FlaG"
    expected = False
    assert solution.detectCapitalUse(word)==expected

def test_solution3():
    solution = Solution()
    word = "Python"
    expected = True
    assert solution.detectCapitalUse(word)==expected

def test_solution4():
    solution = Solution()
    word = "bash"
    expected = True
    assert solution.detectCapitalUse(word)==expected

    