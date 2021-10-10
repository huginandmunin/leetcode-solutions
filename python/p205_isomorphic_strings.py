
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        chars = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            # Check if the source character has already been assigned.
            if s[i] in chars.keys():
                if chars[s[i]] != t[i]:
                    return False
            # If new key then check if this value has already been added for a different key
            elif t[i] in chars.values():
                return False
            else:
                chars[s[i]] = t[i]
            
        return True


      

            