from p3142_check_if_grid_satisfies_conditions import Solution

def test_solution1():
    solution = Solution()
    grid = [[1,0,2],[1,0,2],[1,0,2]]
    expected = True
    assert solution.satisfiesConditions(grid)==expected

def test_solution2():
    solution = Solution()
    grid = [[1,1,1],[0,0,0]]
    expected = False
    assert solution.satisfiesConditions(grid)==expected

def test_solution3():
    solution = Solution()
    grid = [[1],[2],[3]]
    expected = False
    assert solution.satisfiesConditions(grid)==expected