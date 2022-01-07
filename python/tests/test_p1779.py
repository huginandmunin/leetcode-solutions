from p1779_find_nearest_point_that_has_the_same_x_or_y_coordinate import Solution


def test_solution1():
    solution = Solution()
    points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
    x=3
    y=4
    expected=2
    result = solution.nearestValidPoint(x,y,points)
    assert result==expected


def test_solution2():
    # Points has same point as x,y
    solution = Solution()
    points = [[3,4]]
    x=3
    y=4
    expected=0
    result = solution.nearestValidPoint(x,y,points)
    assert result==expected


def test_solution3():
    # No points match
    solution = Solution()
    points = [[2,3]]
    x=3
    y=4
    expected=-1
    result = solution.nearestValidPoint(x,y,points)
    assert result==expected