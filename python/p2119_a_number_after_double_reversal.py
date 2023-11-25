class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        if num == 0:
            return True
        # numerical
        return num % 10 != 0
        # or evaluate last character of number
        # return str(num)[-1] != '0' 
