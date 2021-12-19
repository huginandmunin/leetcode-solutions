from p344_reverse_string import Solution

def test_solution1():
    solution = Solution()
    s = ["h","e","l","l","o"]
    expected = ["o","l","l","e","h"]
    assert solution.reverseString(s)==expected

def test_solution2():
    solution = Solution()
    s = ["H","a","n","n","a","h"]
    expected = ["h","a","n","n","a","H"]
    assert solution.reverseString(s)==expected

def test_solution3():
    solution = Solution()
    s = ["H"]
    expected = ["H"]
    assert solution.reverseString(s)==expected