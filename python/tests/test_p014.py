from p014_longest_common_prefix import Solution


def test_solution1():
    solution = Solution()
    input = ["flower","flow","flight"]
    expected = "fl"
    assert solution.longestCommonPrefix(input)==expected

def test_solution2():
    solution = Solution()
    input = ["dog", "racecar", "car"]
    expected = ""
    assert solution.longestCommonPrefix(input)==expected

def test_solution3():
    solution = Solution()
    input = ["flower", "flower", "flower", "flower"]
    expected = "flower"
    assert solution.longestCommonPrefix(input)==expected

def test_solution4():
    solution = Solution()
    input = ["flower", "", "flower", "flower"]
    expected = ""
    assert solution.longestCommonPrefix(input)==expected