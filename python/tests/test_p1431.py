from p1431_kids_with_the_greatest_number_of_candies import Solution


def test_solution1():
    solution = Solution()
    candies = [2,3,5,1,3]
    n = 3
    expected = [True, True, True, False, True]
    assert solution.kidsWithCandies(candies,n)==expected


def test_solution2():
    solution = Solution()
    candies = [4,2,1,1,2]
    n = 1
    expected = [True, False, False, False, False]
    assert solution.kidsWithCandies(candies,n)==expected


def test_solution1():
    solution = Solution()
    candies = [12,1,12]
    n = 10
    expected = [True, False, True]
    assert solution.kidsWithCandies(candies,n)==expected