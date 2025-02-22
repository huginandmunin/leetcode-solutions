from p2126_destoying_asteroids import Solution

def test_solution1():
    solution = Solution()
    mass = 10
    asteroids = [3,9,19,5,21]
    expected = True
    assert solution.asteroidsDestroyed(mass, asteroids)==expected

def test_solution2():
    solution = Solution()
    mass = 5
    asteroids = [4,9,23,4]
    expected = False
    assert solution.asteroidsDestroyed(mass, asteroids)==expected