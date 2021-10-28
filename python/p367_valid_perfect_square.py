class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """ Utilize the method of p069 square root estimate. 
            Return true if the square is perfect and not rounded down. 
        """
        result = False
        r = 1
        while r * r <= num:
            r += 1
            # You could put in an inner loop for larger increments, eg, r = r + r
        r -= 1

        if r * r == num:
            result = True

        return result