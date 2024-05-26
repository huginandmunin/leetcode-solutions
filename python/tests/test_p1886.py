from p1886_determine_whether_matrix_can_be_obtained_by_rotation import Solution


def test_solution1():
    solution = Solution()
    input = [[0,1],[1,0]]
    target = [[1,0],[0,1]]
    expected = True
    assert solution.findRotation(input, target)==expected

def test_solution2():
    solution = Solution()
    input = [[0,1],[1,1]]
    target = [[1,0],[0,1]]
    expected = False
    assert solution.findRotation(input, target)==expected

def test_solution3():
    solution = Solution()
    input = [[0,0,0],[0,1,0],[1,1,1]]
    target = [[1,1,1],[0,1,0],[0,0,0]]
    expected = True
    assert solution.findRotation(input, target)==expected

def test_solution4():
    solution = Solution()
    input = [[1,1],[0,1]]
    target = [[1,1],[1,0]]
    expected = True
    assert solution.findRotation(input, target)==expected