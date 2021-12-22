from p200_number_of_islands import Solution

def test_solution1():
    solution = Solution()
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    expected = 1
    assert solution.numIslands(grid)==expected

def test_solution2():
    solution = Solution()
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    expected = 3
    assert solution.numIslands(grid)==expected