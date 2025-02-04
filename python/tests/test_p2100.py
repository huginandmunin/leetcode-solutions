from p2100_find_good_days_to_rob_the_bank import Solution

def test_solution1():
    solution = Solution()
    security = [5,3,3,3,5,6,2]
    time = 2
    expected = [2,3]
    assert solution.goodDaysToRobBank(security, time)==expected

def test_solution2():
    solution = Solution()
    security = [1,1,1,1,1]
    time = 0
    expected = [0,1,2,3,4]
    assert solution.goodDaysToRobBank(security, time)==expected

def test_solution3():
    solution = Solution()
    security = [1,2,3,4,5,6]
    time = 2
    expected = []
    assert solution.goodDaysToRobBank(security, time)==expected

def test_solution4():
    solution = Solution()
    security = [1,2,3,4]
    time = 1
    expected = []
    assert solution.goodDaysToRobBank(security, time)==expected