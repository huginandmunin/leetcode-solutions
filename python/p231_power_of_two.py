class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Powers of two in binary are
        0001
        0010
        0100
        1000
        ...

        and these numbers less by 1 are
        0000
        0001
        0011
        0111
        ...

        If n is an integer power of two then performing 
        n AND (n - 1) 
        would give a result of 0.
        For example, if n = 8, then
        8 & (8-1) = 8 & 7 = 1000 & 0111 = 0.
        """
        if n < 1:
            return False
        else:
            return n &(n-1) == 0