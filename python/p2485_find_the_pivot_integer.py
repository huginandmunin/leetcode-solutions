class Solution:
    def pivotInteger(self, n: int) -> int:
        """form prefix array"""
        if n == 1:
            return 1
        
        prefix = []
        sum = 0
        for i in range(1,n+1):
            sum += i
            prefix.append(sum)

        for i in range(1,n):
            if prefix[i] == prefix[n-1] - prefix[i-1]:
                return i+1

            elif prefix[i] > prefix[n-1] - prefix[i-1]:
                break

        return -1