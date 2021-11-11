class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ls = list(s)
        ls.sort()
        lt = list(t)
        lt.sort()
        return ls == lt
        