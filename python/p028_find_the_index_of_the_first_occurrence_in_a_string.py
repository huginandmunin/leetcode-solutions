class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle:
            slice_len = len(needle)
            for i,c in enumerate(haystack):
                # slice haystack and compare with needle
                if needle == haystack[i:i+slice_len]:
                    return i
        return -1
