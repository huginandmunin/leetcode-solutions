from p566_reshape_the_matrix import Solution


def test_solution1():
    solution = Solution()
    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    expected = [[1,2,3,4]]
    assert solution.matrixReshape(mat,r,c)==expected

def test_solution2():
    solution = Solution()
    mat = [[1,2,3,4]]
    r = 2
    c = 2
    expected = [[1,2],[3,4]]
    assert solution.matrixReshape(mat,r,c)==expected


def test_solution3():
    solution = Solution()
    mat = mat = [[1,2],[3,4]]
    r = 2
    c = 4
    expected = [[1,2],[3,4]]
    assert solution.matrixReshape(mat,r,c)==expected