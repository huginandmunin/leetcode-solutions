from p733_flood_fill import Solution

def test_solution1():
    solution = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    expected = [[2,2,2],[2,2,0],[2,0,1]]
    assert solution.floodFill(image,sr,sc,newColor)==expected


def test_solution2():
    solution = Solution()
    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    newColor = 2
    expected = [[2,2,2],[2,2,2]]
    assert solution.floodFill(image,sr,sc,newColor)==expected


def test_solution3():
    solution = Solution()
    image = [[4,4,4],[1,2,1],[4,4,4]]
    sr = 0
    sc = 2
    newColor = 5
    expected = [[5,5,5],[1,2,1],[4,4,4]]
    assert solution.floodFill(image,sr,sc,newColor)==expected


def test_solution4():
    solution = Solution()
    image = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    newColor = 1
    expected = [[0,0,0],[0,1,1]]
    assert solution.floodFill(image,sr,sc,newColor)==expected