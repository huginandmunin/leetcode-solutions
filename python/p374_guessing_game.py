# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """ Perform a binary search by always guessing at midpoint between options. """

        l = 0
        r = n
        mid = self.get_mid(l,r)
        result = self.guess(mid)
        while (result != 0 ):
            if result < 0:
                if (r-l)==1:
                    mid -= 1
                else:
                    r = mid
                    mid = self.get_mid(l,r)
            else:
                if (r-l)==1:
                    mid += 1
                else:
                    l = mid
                    mid = self.get_mid(l,r)
            result = self.guess(mid)
        return mid


    def get_mid(self, left: int, right: int) -> int:
        return (right - left) // 2 + left

    def guess(self, num: int) -> int:

        target = 6
        if num < target:
            return 1
        elif num > target:
            return -1
        else:
            return 0 

if __name__ == '__main__':

    solution = Solution()

    input = 10
    result = solution.guessNumber(input)
    print(f'input={input}, result={result}')