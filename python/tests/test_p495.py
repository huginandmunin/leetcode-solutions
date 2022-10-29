from p495_teamo_attacking import Solution

def test_solution1():
    solution = Solution()
    timeSeries = [1,4]
    duration = 2
    expected = 4
    assert solution.findPoisonedDuration(timeSeries,duration) == expected

def test_solution2():
    solution = Solution()
    timeSeries = [1,2]
    duration = 2
    expected = 3
    assert solution.findPoisonedDuration(timeSeries,duration) == expected

def test_solution3():
    solution = Solution()
    timeSeries = [1,3]
    duration = 4
    expected = 6
    assert solution.findPoisonedDuration(timeSeries,duration) == expected