from p387_first_unique_character_in_a_string import Solution


def test_solution1():
    solution = Solution()
    s = "leetcode"
    expected = 0
    assert solution.firstUniqChar(s)==expected

def test_solution2():
    solution = Solution()
    s = "loveleetcode"
    expected = 2
    assert solution.firstUniqChar(s)==expected

def test_solution3():
    solution = Solution()
    s = "aabb"
    expected = -1
    assert solution.firstUniqChar(s)==expected