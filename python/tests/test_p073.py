from p073_set_matrix_zeros import Solution


def test_solution1():
    solution = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    expected = [[1,0,1],[0,0,0],[1,0,1]]
    assert solution.setZeroes(matrix)==expected

def test_solution2():
    solution = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    expected = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    assert solution.setZeroes(matrix)==expected