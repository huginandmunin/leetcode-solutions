from p2423_remove_letter_to_equalize_frequency import Solution

def test_solution1():
    solution = Solution()
    word = "abcc"
    expected = True
    assert solution.equalFrequency(word)==expected

def test_solution2():
    solution = Solution()
    word = "aazz"
    expected = False
    assert solution.equalFrequency(word)==expected

def test_solution3():
    solution = Solution()
    word = "bac"
    expected = True
    assert solution.equalFrequency(word)==expected

def test_solution4():
    solution = Solution()
    word = "ddaccb"
    expected = False
    assert solution.equalFrequency(word)==expected

def test_solution5():
    solution = Solution()
    word = "cccaa"
    expected = True
    assert solution.equalFrequency(word)==expected