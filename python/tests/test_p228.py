import sys
sys.path.append("..")

from p228_summary_ranges import Solution


def test_solution1():
    solution = Solution()
    nums = [0,1,2,4,5,7]
    expected = ["0->2","4->5","7"]
    assert solution.summaryRanges(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [0,2,3,4,6,8,9]
    expected = ["0","2->4","6","8->9"]
    assert solution.summaryRanges(nums)==expected

def test_solution3():
    solution = Solution()
    nums = []
    expected = []
    assert solution.summaryRanges(nums)==expected

def test_solution4():
    solution = Solution()
    nums = [-1]
    expected = ["-1"]
    assert solution.summaryRanges(nums)==expected

def test_solution5():
    solution = Solution()
    nums = [0]
    expected = ["0"]
    assert solution.summaryRanges(nums)==expected