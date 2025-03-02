from p2570_merge_two_2D_arrays_by_summing_values import Solution


def test_solution1():
    solution = Solution()
    nums1 = [[1,2],[2,3],[4,5]]
    nums2 = [[1,4],[3,2],[4,1]]
    expected = [[1,6],[2,3],[3,2],[4,6]]
    assert solution.mergeArrays(nums1, nums2)==expected

def test_solution2():
    solution = Solution()
    nums1 = [[2,4],[3,6],[5,5]]
    nums2 = [[1,3],[4,3]]
    expected = [[1,3],[2,4],[3,6],[4,3],[5,5]]
    assert solution.mergeArrays(nums1, nums2)==expected
