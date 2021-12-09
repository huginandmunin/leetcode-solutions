class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Store the unique characters in a dict with
        { c1: {'first_i': index, 'count': count}, c2: {...}, ...}
        Select the minimum index where count == 1. 

        A faster solution would be to enumerate s and
        return first index where s.count(c)==1. 
        """
        count_dict = {}
        indexes =[]    
        for i,c in enumerate(s):
            if c in count_dict.keys():
                count_dict[c]['count'] += 1
            else:
                count_dict[c] = {'first_i': i, 'count': 1}
        indexes = [count_dict[c]['first_i'] for c in s if count_dict[c]['count']==1]
        
        if len(indexes)==0:
            return -1
        else:
            return indexes.pop(0)
