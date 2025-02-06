class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True
        if len(s1) == 1:
            return False
        
        s1_set = set()
        s2_set = set()
        difference_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                difference_count += 1
                s1_set.add(s1[i])
                s2_set.add(s2[i])
            if difference_count > 2:
                return False
            
        if difference_count not in [0,2]:
            return False
        if s1_set == s2_set:
            return True
        else:
            return False