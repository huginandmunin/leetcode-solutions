from p575_distribute_candies import Solution


def test_solution1():
    solution = Solution()
    candyType = [1,1,2,2,3,3]
    expected = 3
    assert solution.distributeCandies(candyType)==expected

def test_solution2():
    solution = Solution()
    candyType = [1,1,2,3]
    expected = 2
    assert solution.distributeCandies(candyType)==expected

def test_solution3():
    solution = Solution()
    candyType = [6,6,6,6]
    expected = 1
    assert solution.distributeCandies(candyType)==expected