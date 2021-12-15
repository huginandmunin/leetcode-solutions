import sys
sys.path.append("..")

from p500_keyboard_row import Solution

def test_solution1():
    solution = Solution()
    words = ["Hello","Alaska","Dad","Peace"]
    expected = ["Alaska","Dad"]
    assert solution.findWords(words)==expected

def test_solution2():
    solution = Solution()
    words = ["omk"]
    expected = []
    assert solution.findWords(words)==expected

def test_solution3():
    solution = Solution()
    words = ["adsdf","sfd"]
    expected = ["adsdf","sfd"]
    assert solution.findWords(words)==expected

def test_solution4():
    solution = Solution()
    words = ["a","b"]
    expected = ["a","b"]
    assert solution.findWords(words)==expected