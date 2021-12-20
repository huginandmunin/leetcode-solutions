from p463_island_perimeter import Solution

def test_solution1():
    solution = Solution()
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    expected = 16
    assert solution.islandPerimeter(grid)==expected

def test_solution2():
    solution = Solution()
    grid = [[1]]
    expected = 4
    assert solution.islandPerimeter(grid)==expected

def test_solution3():
    solution = Solution()
    grid = [[1,0]]
    expected = 4
    assert solution.islandPerimeter(grid)==expected