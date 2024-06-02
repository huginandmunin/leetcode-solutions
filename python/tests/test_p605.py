from p605_can_place_flowers import Solution


def test_solution1():
    solution = Solution()
    flowerbed = [1,0,0,0,1]
    n = 1
    expected = True
    assert solution.canPlaceFlowers(flowerbed, n)==expected

def test_solution2():
    solution = Solution()
    flowerbed = [1,0,0,0,1]
    n = 2
    expected = False
    assert solution.canPlaceFlowers(flowerbed, n)==expected

def test_solution3():
    solution = Solution()
    flowerbed = [1,0,0,0,1,0,0]
    n = 2
    expected = True
    assert solution.canPlaceFlowers(flowerbed, n)==expected

def test_solution4():
    solution = Solution()
    flowerbed = [0]
    n = 1
    expected = True
    assert solution.canPlaceFlowers(flowerbed, n)==expected

def test_solution5():
    solution = Solution()
    flowerbed = [0, 0]
    n = 1
    expected = True
    assert solution.canPlaceFlowers(flowerbed, n)==expected

def test_solution6():
    solution = Solution()
    flowerbed = [0, 0]
    n = 2
    expected = False
    assert solution.canPlaceFlowers(flowerbed, n)==expected