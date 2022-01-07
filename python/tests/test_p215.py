from p215_kth_largest_element import Solution


def test_solution1():
    solution = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    expected = 5
    assert solution.findKthLargest(nums,k)==expected

def test_solution2():
    solution = Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    expected = 4
    assert solution.findKthLargest(nums,k)==expected

def test_solution3():
    solution = Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    k = 1
    expected = 6
    assert solution.findKthLargest(nums,k)==expected

def test_solution4():
    solution = Solution()
    nums = [3]
    k = 1
    expected = 3
    assert solution.findKthLargest(nums,k)==expected