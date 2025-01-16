from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
        The XOR is an associated operator so we can think of re-arranging
        the order of the operands, in particular the number of times that any
        number is repeated. A number that XORs with itself an even number will result
        in 0, and an odd number will result in the same number.

        So if an array length is an even number, the other numbers do not contribute to the
        the result. If an array length is an odd number then we XOR the numbers in the 
        other array. 

        For example, for the two arrays
        [a,b], [c,d]

        we can write out equivalent sets of operations

        a^c ^ a^d ^ b^c ^ b^d
        a ^ c ^ a ^ d ^ b ^ c ^ d ^ d
        a^a ^ b^b ^ c^c ^ d^d
        0 ^ 0 ^ 0 ^ 0 ^
        0
        """

        result = 0
        if (len(nums2) % 2):
            for num in nums1:
                result = result ^ num

        if (len(nums1) % 2):
            for num in nums2:
                result = result ^ num

        return result
    