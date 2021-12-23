from p661_image_smoother import Solution

def test_solution1():
    solution = Solution()
    img = [[1,1,1],[1,0,1],[1,1,1]]
    expected = [[0,0,0],[0,0,0],[0,0,0]]
    assert solution.imageSmoother(img)==expected

def test_solution2():
    solution = Solution()
    img = [[100,200,100],[200,50,200],[100,200,100]]
    expected = [[137,141,137],[141,138,141],[137,141,137]]
    assert solution.imageSmoother(img)==expected
