from p1624_largest_substring_between_two_equal_characters import Solution

def test_solution1():
    solution = Solution()
    s = 'aa'
    expected = 0
    assert solution.maxLengthBetweenEqualCharacters(s)==expected

def test_solution2():
    solution = Solution()
    s = 'abca'
    expected = 2
    assert solution.maxLengthBetweenEqualCharacters(s)==expected

def test_solution2():
    solution = Solution()
    s = 'cbzxy'
    expected = -1
    assert solution.maxLengthBetweenEqualCharacters(s)==expected

