from p2017_grid_game import Solution


def test_solution1():
    solution = Solution()
    grid = [[2,5,4],[1,5,1]]
    expected = 4
    assert solution.gridGame(grid)==expected

def test_solution2():
    solution = Solution()
    grid = grid = [[3,3,1],[8,5,2]]
    expected = 4
    assert solution.gridGame(grid)==expected

def test_solution3():
    solution = Solution()
    grid = grid = [[1,3,1,15],[1,3,3,1]]
    expected = 7
    assert solution.gridGame(grid)==expected

def test_solution4():
    solution = Solution()
    grid = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]
    expected = 63
    assert solution.gridGame(grid)==expected

def test_solution5():
    solution = Solution()
    grid = [[1], [2]]
    expected = 0
    assert solution.gridGame(grid)==expected

def test_solution6():
    solution = Solution()
    grid = [[1, 1], [2, 2]]
    expected = 1
    assert solution.gridGame(grid)==expected