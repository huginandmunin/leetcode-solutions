from p2460_apply_operations_to_array import Solution

def test_solution1():
    solution = Solution()
    nums = [1,2,2,1,1,0]
    expected = [1,4,2,0,0,0]
    assert solution.applyOperations(nums)==expected
    
def test_solution2():
    solution = Solution()
    nums = [0,1]
    expected = [1,0]
    assert solution.applyOperations(nums)==expected