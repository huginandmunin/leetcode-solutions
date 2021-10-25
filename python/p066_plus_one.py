from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """ Start at least significant digit and add 1 until there is no carry value """
        carry = 1
        i = len(digits)-1
        while carry == 1 and i >= 0:
            if (digits[i] == 9):
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
            i -= 1

        if carry:
            digits = [carry] + digits

        return digits

