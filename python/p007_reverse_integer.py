class Solution(object):
    """
    The mathematical solution is presented.

    A string approach is what I would most likely use.
    """
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x is None or x == 0:
            return x

        sign = 1
        # Change negative to positive
        if x < 0:
            sign = -1
            x = x * sign
        # Initialize with least significant digit
        new_digit = x % 10
        result = new_digit
        x = int((x - new_digit) /10)
        # Iterate through least-significant to most-significant digits
        while x > 0:
            new_digit = x%10
            result = result*10 + new_digit
            x = int((x - new_digit) /10)
        
        result = sign * result
        if result > (2**31-1) or result < -2**31:
            result = 0
        return result
      