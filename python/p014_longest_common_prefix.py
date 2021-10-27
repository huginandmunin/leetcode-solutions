from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ Take the first string and store as a potential prefix.
            Check succeeding strings for number of characters matched with the saved prefix. 
        """
        plist = []
        if strs:
            plist = list(strs.pop(0))

        while plist and strs:
            nlist = list(strs.pop(0))
            if nlist != plist:
                # Find longest prefix between nlist and plist
                i = 1
                while nlist[0:i] == plist[0:i] and i <= len(plist):
                    i += 1
                # Adjust length of prefix to new match (handle the extra increment)
                plist = plist[0:i-1]

        return ''.join(plist)

