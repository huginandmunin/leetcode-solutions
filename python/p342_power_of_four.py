class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 4 > 0:
            return False

        while n > 0:
            if n % 4 == 0:
                n = n / 4
                if n == 1:
                    return True
                if n < 4:
                    return False
            else:
                return False