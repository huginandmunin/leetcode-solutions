from p1513_number_of_substrings_with_only_1s import Solution

def test_solution1():
    solution = Solution()
    s = "0110111"
    expected = 9
    assert solution.numSub(s)==expected

def test_solution2():
    solution = Solution()
    s = "101"
    expected = 2
    assert solution.numSub(s)==expected

def test_solution3():
    solution = Solution()
    s = "111111"
    expected = 21
    assert solution.numSub(s)==expected

def test_solution4():
    solution = Solution()
    s = "000"
    expected = 0
    assert solution.numSub(s)==expected