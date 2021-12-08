import sys
sys.path.append("..")

from p771_jewels_and_stones import Solution


def test_solution1():
    solution = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    expected = 3
    assert solution.numJewelsInStones(jewels,stones)==expected


def test_solution2():
    solution = Solution()
    jewels = "z"
    stones = "ZZ"
    expected = 0
    assert solution.numJewelsInStones(jewels,stones)==expected