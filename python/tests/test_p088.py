from p088_merge_sorted_array import Solution

def test_solution1():
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    expected = [1, 2, 2, 3, 5, 6]
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')
    assert nums1==expected

def test_solution2():
    solution = Solution()
    nums1 = [6,7,8,0,0,0,0]
    m = 3
    nums2 = [1,2,3,4]
    n = 4
    expected = [1, 2, 3, 4, 6, 7, 8]
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')
    assert nums1==expected

def test_solution3():
    solution = Solution()
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    expected = [1]
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')
    assert nums1==expected

def test_solution4():
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    expected = [1, 2, 2, 3, 5, 6]
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')
    assert nums1==expected

def test_solution5():
    solution = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    expected = [1]
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')
    assert nums1==expected

def test_solution6():
    solution = Solution()
    nums1 = [1,0]
    m = 1
    nums2 = [2]
    n = 1
    expected = [1, 2]
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')
    assert nums1==expected

def test_solution7():
    solution = Solution()
    nums1 = [1,2,4,5,6,0]
    m = 5
    nums2 = [3]
    n = 1
    expected = [1, 2, 3, 4, 5, 6]
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')
    assert nums1==expected

