import sys
sys.path.append("..")

from p1103_distribute_candies_to_people import Solution


def test_solution1():
    solution = Solution()
    candies = 7
    num_people = 4
    expected = [1,2,3,1]
    assert solution.distributeCandies(candies,num_people)==expected


def test_solution2():
    solution = Solution()
    candies = 10
    num_people = 3
    expected = [5,2,3]
    assert solution.distributeCandies(candies,num_people)==expected


def test_solution3():
    solution = Solution()
    candies = 3
    num_people = 5
    expected = [1,2,0,0,0]
    assert solution.distributeCandies(candies,num_people)==expected


def test_solution4():
    solution = Solution()
    candies = 3
    num_people = 1
    expected = [3]
    assert solution.distributeCandies(candies,num_people)==expected