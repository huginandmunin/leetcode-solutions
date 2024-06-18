from p735_asteroid_collision import Solution

def test_solution1():
    solution = Solution()
    asteroids = [5,10,-5]
    expected = [5,10]
    assert solution.asteroidCollision(asteroids) == expected

def test_solution2():
    solution = Solution()
    asteroids = [1,1,2,1,1,-2]
    expected = [1,1]
    assert solution.asteroidCollision(asteroids) == expected

def test_solution3():
    solution = Solution()
    asteroids = [1,3,2,2,2,1,1,-2]
    expected = [1,3,2,2]
    assert solution.asteroidCollision(asteroids) == expected

def test_solution4():
    solution = Solution()
    asteroids = [5,2,-1,-5,3]
    expected = [3]
    assert solution.asteroidCollision(asteroids) == expected

def test_solution5():
    solution = Solution()
    asteroids = [5,-1,-1]
    expected = [5]
    assert solution.asteroidCollision(asteroids) == expected