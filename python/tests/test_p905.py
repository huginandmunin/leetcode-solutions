from p905_sort_array_by_parity import Solution

def test_solution1():
    solution = Solution()
    nums = [3,1,2,4]
    expected =[4,2,3,1]
    assert solution.sortArrayByParity(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [0]
    expected =[0]
    assert solution.sortArrayByParity(nums)==expected