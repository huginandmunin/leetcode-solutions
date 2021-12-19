# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        Perform a binary search by always guessing at midpoint between options. 
        """

        l = 1
        r = n
        mid = self.get_mid(l,r)
        result = self.isBadVersion(mid)
        found = False
        while (not found):
            if result:
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
            result = self.isBadVersion(mid)
            if (result and (abs(r-l)<=1) ):
                found = True
        return mid


    def get_mid(self, left: int, right: int) -> int:
        return (right - left) // 2 + left

        
    def isBadVersion(self, num: int) -> bool:
        target = 4 # set to match unit tests
        if num < target:
            return False
        elif num >= target:
            return True
