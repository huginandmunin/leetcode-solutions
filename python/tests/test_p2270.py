from p2270_number_of_ways_to_split_array import Solution

def test_solution1():
    solution = Solution()
    nums = [10,4,-8,7]
    expected = 2
    assert solution.waysToSplitArray(nums)==expected


def test_solution2():
    solution = Solution()
    nums = [2,3,1,0]
    expected = 2
    assert solution.waysToSplitArray(nums)==expected

def test_solution3():
    solution = Solution()
    nums = [1,2,0,3]
    expected = 2
    assert solution.waysToSplitArray(nums)==expected

def test_solution4():
    solution = Solution()
    nums = [1,1,0,3]
    expected = 0
    assert solution.waysToSplitArray(nums)==expected