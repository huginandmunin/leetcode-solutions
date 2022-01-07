from p1992_find_all_groups_of_farmland import Solution

def test_solution1():
    solution = Solution()
    land = [[1,0,0],[0,1,1],[0,1,1]]
    expected = [[0,0,0,0],[1,1,2,2]]
    assert solution.findFarmland(land)==expected

def test_solution2():
    solution = Solution()
    land = land = [[1,1],[1,1]]
    expected = [[0,0,1,1]]
    assert solution.findFarmland(land)==expected

def test_solution3():
    solution = Solution()
    land = [[0]]
    expected = []
    assert solution.findFarmland(land)==expected