from p1572_matrix_diagonal_sum import Solution

def test_solution1():
    solution = Solution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    expected = 25
    assert solution.diagonalSum(mat)==expected

def test_solution2():
    solution = Solution()
    mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    expected = 8
    assert solution.diagonalSum(mat)==expected

def test_solution3():
    solution = Solution()
    mat = [[5]]
    expected = 5
    assert solution.diagonalSum(mat)==expected