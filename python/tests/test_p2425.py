from p2425_Bitwise_XOR_of_all_pairings import Solution

def test_solution1():
    solution = Solution()
    nums1 = [2,1,3]
    nums2 = [10,2,5,0]
    expected = 13
    assert solution.xorAllNums(nums1, nums2)==expected


def test_solution2():
    solution = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    expected = 0
    assert solution.xorAllNums(nums1, nums2)==expected