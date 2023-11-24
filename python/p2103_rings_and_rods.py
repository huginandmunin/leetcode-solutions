class Solution:
    def countPoints(self, rings: str) -> int:
 
        total = 0
        # Store the counts in a dict of dicts
        counts = {}
        for i in range(10):
            counts[i] = { "R": 0, "G": 0, "B": 0}
        # There are probably more efficient methods for parsing the string, eg, regex
        list = [x for x in rings]
        while list:
            color = list.pop(0)
            rod = int(list.pop(0))
            counts[rod][color] += 1

        for c in counts:
            if counts[c]['R'] and counts[c]['G'] and counts[c]['B']:
                total += 1
       
        return total
 