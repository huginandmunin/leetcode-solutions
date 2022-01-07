from p973_k_closest_points import Solution


def test_solution1():
    solution = Solution()
    points = [[1,3],[-2,2]]
    k=1
    expected=[[-2, 2]]
    result = solution.kClosest(points,k)
    assert result==expected


def test_solution2():
    solution = Solution()
    points = [[3, 3], [5, -1], [-2, 4]]
    k=2
    expected=[[3, 3], [-2, 4]]
    result = solution.kClosest(points,k)
    assert result==expected


def test_solution3():
    solution = Solution()
    points = [[3, 3], [5, -1], [-2, 4]]
    k=0
    expected=[]
    result = solution.kClosest(points,k)
    assert result==expected


def test_solution4():
    solution = Solution()
    points = []
    k=4
    expected=[]
    result = solution.kClosest(points,k)
    assert result==expected