class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1 or n % 3 > 0:
            return False

        while n > 0:
            if n % 3 == 0:
                n = n / 3
                if n == 1:
                    return True
            else:
                return False

        return False