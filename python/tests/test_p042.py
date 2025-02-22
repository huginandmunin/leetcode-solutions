from p042_trapping_rain_water import Solution


def test_solution1():
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    expected = 6
    assert solution.trap(height)==expected

def test_solution2():
    solution = Solution()
    height = [4,2,0,3,2,5]
    expected = 9
    assert solution.trap(height)==expected