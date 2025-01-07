from collections import Counter
from p1408_string_matching_in_an_array import Solution

# Change the sort to use Counter
def test_solution1():
    solution = Solution()
    words = ["mass","as","hero","superhero"]
    expected=["hero", "as"]
    assert Counter(solution.stringMatching(words))==Counter(expected)

def test_solution2():
    solution = Solution()
    words = ["leetcode","et","code"]
    expected=["et","code"]
    assert Counter(solution.stringMatching(words))==Counter(expected)

def test_solution3():
    solution = Solution()
    words = ["blue","green","bu"]
    expected=[]
    assert Counter(solution.stringMatching(words))==Counter(expected)