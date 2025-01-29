from p1094_car_pooling import Solution

def test_solution1():
    solution = Solution()
    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    expected = False
    assert solution.carPooling(trips, capacity)==expected

def test_solution2():
    solution = Solution()
    trips = [[2,1,5],[3,3,7]]
    capacity = 5
    expected = True
    assert solution.carPooling(trips, capacity)==expected

def test_solution3():
    solution = Solution()
    trips = [[2,1,5],[3,5,7]]
    capacity = 3
    expected = True
    assert solution.carPooling(trips, capacity)==expected