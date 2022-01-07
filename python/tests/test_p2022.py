from p2022_convert_1d_array_into_2d_array import Solution

def test_solution1():
    solution = Solution()
    original = [1,2,3,4]
    m = 2
    n = 2
    expected = [[1,2],[3,4]]
    assert solution.construct2DArray(original,m,n)==expected

def test_solution2():
    solution = Solution()
    original = [1,2,3]
    m = 1
    n = 3
    expected = [[1,2,3]]
    assert solution.construct2DArray(original,m,n)==expected

def test_solution3():
    solution = Solution()
    original = [1,2]
    m = 1
    n = 1
    expected = []
    assert solution.construct2DArray(original,m,n)==expected