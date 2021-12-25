from p074_search_a_2d_matrix import Solution


def test_solution1():
    solution = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 0
    expected = False
    assert solution.searchMatrix(matrix, target)==expected

def test_solution2():
    solution = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 100
    expected = False
    assert solution.searchMatrix(matrix, target)==expected

def test_solution3():
    solution = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    expected = True
    assert solution.searchMatrix(matrix, target)==expected

def test_solution4():
    solution = Solution()
    matrix = matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    expected = False
    assert solution.searchMatrix(matrix, target)==expected

def test_solution5():
    solution = Solution()
    matrix = matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 60
    expected = True
    assert solution.searchMatrix(matrix, target)==expected

def test_solution6():
    solution = Solution()
    matrix = matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 23
    expected = True
    assert solution.searchMatrix(matrix, target)==expected

def test_solution7():
    solution = Solution()
    matrix = matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 8
    expected = False
    assert solution.searchMatrix(matrix, target)==expected

def test_solution8():
    solution = Solution()
    matrix = matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 11
    expected = True
    assert solution.searchMatrix(matrix, target)==expected

def test_solution9():
    solution = Solution()
    matrix = matrix = [[1,3]]
    target = 3
    expected = True
    assert solution.searchMatrix(matrix, target)==expected