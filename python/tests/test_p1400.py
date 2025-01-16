from p1400_construct_k_palindrome_strings import Solution

# Change the sort to use Counter
def test_solution1():
    solution = Solution()
    s = "annabelle"
    k = 2
    expected = True
    assert solution.canConstruct(s, k) == expected

def test_solution2():
    solution = Solution()
    s = "leetcode"
    k = 3
    expected = False
    assert solution.canConstruct(s, k) == expected

def test_solution3():
    solution = Solution()
    s = "true"
    k = 4
    expected = True
    assert solution.canConstruct(s, k) == expected