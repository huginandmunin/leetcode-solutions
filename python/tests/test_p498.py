from p498_diagonal_traverse import Solution

def test_solution1():
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    expected = [1,2,4,7,5,3,6,8,9]
    assert solution.findDiagonalOrder(matrix)==expected

def test_solution2():
    solution = Solution()
    matrix = [[1,2],[3,4]]
    expected = [1,2,3,4]
    assert solution.findDiagonalOrder(matrix)==expected

def test_solution3():
    solution = Solution()
    matrix = [[1]]
    expected = [1]
    assert solution.findDiagonalOrder(matrix)==expected