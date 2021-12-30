from p054_spiral_matrix import Solution


def test_solution1():
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    expected = [1,2,3,6,9,8,7,4,5]
    assert solution.spiralOrder(matrix)==expected


def test_solution2():
    solution = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    expected = [1,2,3,4,8,12,11,10,9,5,6,7]
    assert solution.spiralOrder(matrix)==expected

def test_solution3():
    solution = Solution()
    matrix = [[3],[2]]
    expected = [3,2]
    assert solution.spiralOrder(matrix)==expected