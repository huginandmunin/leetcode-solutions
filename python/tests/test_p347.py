import sys
sys.path.append("..")

from p347_top_k_frequent_elements import Solution


def test_solution1():
    solution = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    expected = [1,2]
    assert solution.topKFrequent(nums,k)==expected

def test_solution2():
    solution = Solution()
    nums = [1]
    k = 1
    expected = [1]
    assert solution.topKFrequent(nums,k)==expected

def test_solution3():
    solution = Solution()
    nums = [1,10,2,10,3,10,99,99,99,99]
    k = 2
    expected = [99,10]
    assert solution.topKFrequent(nums,k)==expected