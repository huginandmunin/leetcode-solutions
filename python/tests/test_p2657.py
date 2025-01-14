from p2657_find_the_prefix_common_array_of_two_arrays import Solution

def test_solution1():
    solution = Solution()
    A = [1,3,2,4]
    B = [3,1,2,4]
    expected = [0,2,3,4]
    assert solution.findThePrefixCommonArray(A, B)==expected

def test_solution2():
    solution = Solution()
    A = [2,3,1]
    B = [3,1,2]
    expected = [0,1,3]
    assert solution.findThePrefixCommonArray(A, B)==expected