from p349_intersection_of_two_arrays import Solution

def test_solution1():
    solution = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    expected = [2]
    assert solution.intersection(nums1, nums2)==expected

def test_solution2():
    solution = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    expected = [9,4]
    assert solution.intersection(nums1, nums2)==expected