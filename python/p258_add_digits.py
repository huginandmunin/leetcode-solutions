class Solution:
    def addDigits(self, num: int) -> int:
        """
        Given an integer num, repeatedly add all its digits 
        until the result has only one digit, and return it.
        Recursion gives a python depth limit error, so implement as a while statement.
        This solution sums the digits mathematically. You could also do some str/int conversion.
        """

        while num >= 10:
            # Sum digits starting with least significant
            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10
            # Swap out sum and num
            num = sum

        return num


if __name__ == "__main__":
    solution = Solution()
    num = 38
    result = solution.addDigits(num)
    print(f'num={num}, result={result}')

    num = 0
    result = solution.addDigits(num)
    print(f'num={num}, result={result}')