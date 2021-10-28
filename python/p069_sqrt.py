class Solution:
    def mySqrt(self, x: int) -> int:
        """ Find integer portion of square root by brute force.
            Start at 1 and go up. For larger numbers this becomes
            more efficient that going down (from say x/2).

            Another option would be the Babylonian method.
            https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
            r_n+1 = 1/2( r_n + x/r_n )

        """
        r = 1
        while r * r <= x:
            r += 1
        r -= 1

        return r
