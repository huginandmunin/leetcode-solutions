import sys
sys.path.append("..")

from p1636_sort_array_by_increasing_frequency import Solution


def test_solution1():
    solution = Solution()
    nums = [1,1,2,2,2,3]
    expected = [3,1,1,2,2,2]
    assert solution.frequencySort(nums)==expected


def test_solution2():
    solution = Solution()
    nums = [2,3,1,3,2]
    expected = [1,3,3,2,2]
    assert solution.frequencySort(nums)==expected


def test_solution3():
    solution = Solution()
    nums = [-1,1,-6,4,5,-6,1,4,1]
    expected = [5,-1,4,4,-6,-6,1,1,1]
    assert solution.frequencySort(nums)==expected