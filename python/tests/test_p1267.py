from p1267_count_servers import Solution


def test_solution1():
    solution = Solution()
    grid = [[1,0],[0,1]]
    expected = 0
    assert solution.countServers(grid)==expected

def test_solution2():
    solution = Solution()
    grid = [[1,0],[1,1]]
    expected = 3
    assert solution.countServers(grid)==expected

def test_solution3():
    solution = Solution()
    grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    expected = 4
    assert solution.countServers(grid)==expected

def test_solution4():
    solution = Solution()
    grid = [[1,1,0,0],[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,1]]
    expected = 4
    assert solution.countServers(grid)==expected

def test_solution5():
    solution = Solution()
    grid = [[0,0,0,0],[1,1,1,1],[0,0,0,1],[0,0,1,1],[0,0,0,1]]
    expected = 8
    assert solution.countServers(grid)==expected