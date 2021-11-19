from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        The solution below implements element-by-element comparisons.
        A real-life solution would be to insert nums2 into nums1 and do a sort.
        """

        # Shift nums1 to put the 0's first
        if m > 0 and n > 0:
            for i in range(m+n-1,-1,-1):
                nums1[i]=nums1[i-n]
            for i in range(n):
                nums1[i]=0

        i = 0
        j = 0
        new = 0
        while i < m and j < n:
            if nums1[i+n] < nums2[j]:
                nums1[new] = nums1[i+n]
                i += 1
            else:
                nums1[new] = nums2[j]
                j += 1
            new += 1
        if i == m:
            while j < n:
                nums1[new] = nums2[j]
                j += 1
                new += 1
        nums1 = nums1

        return None


if __name__ == '__main__':

    solution = Solution()

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')

    nums1 = [6,7,8,0,0,0,0]
    m = 3
    nums2 = [1,2,3,4]
    n = 4
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')

    nums1 = [1,0]
    m = 1
    nums2 = [2]
    n = 1
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')

    nums1 = [1,2,4,5,6,0]
    m = 5
    nums2 = [3]
    n = 1
    solution.merge(nums1,m,nums2,n)
    print(f'nums1 = {nums1}')

