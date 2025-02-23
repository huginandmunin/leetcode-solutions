from p2364_count_number_of_bad_pairs import Solution


def test_solution1():
    solution = Solution()
    nums = [4,1,3,3]
    expected = 5
    assert solution.countBadPairs(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [1,2,3,4,5]
    expected = 0
    assert solution.countBadPairs(nums)==expected

