from p1759_count_number_of_homogeneous_substrings import Solution

def test_solution1():
    solution = Solution()
    s = "abbcccaa"
    expected = 13
    assert solution.countHomogeneous(s)==expected

def test_solution2():
    solution = Solution()
    s = "xy"
    expected = 2
    assert solution.countHomogeneous(s)==expected

def test_solution3():
    solution = Solution()
    s = "zzzzz"
    expected = 15
    assert solution.countHomogeneous(s)==expected