import sys
sys.path.append("..")

from p242_valid_anagram import Solution


def test_solution1():
    solution = Solution()
    s = 'anagram'
    t = 'nagaram'
    assert solution.isAnagram(s,t)==True

def test_solution2():
    solution = Solution()
    s = 'rat'
    t = 'car'
    assert solution.isAnagram(s,t)==False

def test_solution3():
    solution = Solution()
    s = 'banana'
    t = 'annaba'
    assert solution.isAnagram(s,t)==True

def test_solution4():
    solution = Solution()
    s = 'Ahoy'
    t = 'There'
    assert solution.isAnagram(s,t)==False