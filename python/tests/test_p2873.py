from p2873_maximum_value_of_an_ordered_triplet import Solution

def test_solution1():
    solution = Solution()
    nums = [12,6,1,2,7]
    expected = 77
    assert solution.maximumTripletValue(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [1,10,3,4,19]
    expected = 133
    assert solution.maximumTripletValue(nums)==expected

def test_solution3():
    solution = Solution()
    nums = [1,2,3]
    expected = 0
    assert solution.maximumTripletValue(nums)==expected