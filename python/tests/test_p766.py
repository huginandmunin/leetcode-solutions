from p766_toeplitz_matrix import Solution

def test_solution1():
    solution = Solution()
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    expected = True
    assert solution.isToeplitzMatrix(matrix)==expected

def test_solution2():
    solution = Solution()
    matrix = [[1,2],[2,2]]
    expected = False
    assert solution.isToeplitzMatrix(matrix)==expected

def test_solution3():
    solution = Solution()
    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    expected = True
    assert solution.isToeplitzMatrix(matrix)==expected

def test_solution4():
    solution = Solution()
    matrix = [[0,0,0],[0,0,0],[0,0,1]]
    expected = False
    assert solution.isToeplitzMatrix(matrix)==expected