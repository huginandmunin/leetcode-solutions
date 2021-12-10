import sys
sys.path.append("..")

from p451_sort_characters_by_frequency import Solution


def test_solution1():
    solution = Solution()
    s = "tree"
    expected = "eert"
    assert solution.frequencySort(s)==expected

def test_solution2():
    solution = Solution()
    s = "cccaaa"
    expected = "aaaccc"
    assert solution.frequencySort(s)==expected

def test_solution3():
    solution = Solution()
    s = "Aabb"
    expected = "bbAa"
    assert solution.frequencySort(s)==expected

def test_solution4():
    solution = Solution()
    s = "leetcode"
    expected = "eeecdlot"
    assert solution.frequencySort(s)==expected