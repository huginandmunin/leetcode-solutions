from p1726_tuple_with_same_product import Solution

def test_solution1():
    solution = Solution()
    nums = [2,3,4,6]
    expected = 8
    assert solution.tupleSameProduct(nums)==expected

def test_solution2():
    solution = Solution()
    nums = [1,2,4,5,10]
    expected = 16
    assert solution.tupleSameProduct(nums)==expected

def test_solution3():
    solution = Solution()
    nums = [2,3,4,6,8,12]
    expected = 40
    assert solution.tupleSameProduct(nums)==expected