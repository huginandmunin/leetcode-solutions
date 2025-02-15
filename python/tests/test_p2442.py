from p2442_Count_Number_of_Distinct_Integers import Solution

def test_solution1():
    solution = Solution()
    nums = [1,13,10,12,31]
    expected = 6
    assert solution.countDistinctIntegers(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [2,2,2]
    expected = 1
    assert solution.countDistinctIntegers(nums)==expected