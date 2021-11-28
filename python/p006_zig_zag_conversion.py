class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        This solution implements a dictionary to determine indexes for
        pulling characters from s and assigning to each row.
        An alternate approach would be to implement a for-loop to
        zig-zag through the input without using indexes. 
        """

        if numRows < 2 or numRows >= len(s):
            return s

        result = ""
        # Get dictionary of jumps for each row.
        jumps = self.get_jumps_dict(numRows)

        # Use jumps dictionary to pull characters of s
        sl = list(s)
        for i in range(numRows):
            result += self.get_results_for_row(sl,i,jumps)

        return result


    def get_jumps_dict(self,rows):
        """ 
        The jumps dictionary defines the number of characters to skip over
        on each row. The jump for the top row is max = 2*numRows-2. 
        The next jumps alternate between j1 and j2, 
        where j1=max-2, j2=0+2, ...
        """
        jumps = {}
        max = 2 * rows - 2
        j1 = max
        j2 = 0
        for r in range(rows):
            jumps[r] = { "j1": j1, "j2": j2}
            j1 -= 2
            j2 += 2
        # set end points
        jumps[0]["j2"] = max
        jumps[rows-1]["j1"] = max
        return jumps

    
    def get_results_for_row(self,sl,r,jumps):
        result = ""
        max_j = len(sl)
        j = r
        use_j1 = True
        while j < max_j:
            result += sl[j]
            if use_j1: 
                j += jumps[r]["j1"]
            else:
                j += jumps[r]["j2"]
            use_j1 = not use_j1
        return result

