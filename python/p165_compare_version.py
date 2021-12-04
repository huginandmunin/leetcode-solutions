class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Given two version numbers, eg, version1 = "1.01", version2 = "1.001", compare them.

        If version1 < version2, return -1.
        If version1 > version2, return 1.
        Otherwise, return 0.

        """

        v1l = [int(x) for x in version1.split('.')]
        v2l = [int(x) for x in version2.split('.')]        
        min_len = min(len(v1l),len(v2l))
        print(f'min={min_len}, v1l={v1l}, v2l={v2l}')
        for i in range(min_len):
            print(f'i={i}, v1l={v1l[i]}, v2l={v2l[i]}')
            if v1l[i] < v2l[i]:
                return -1
            elif v1l[i] > v2l[i]:
                return 1

        # Handle the longer version number, looking for any tag > 0
        if len(v1l) > min_len:
            for k in range(i+1,len(v1l)): 
                print(f'k={k}, v1l={v1l[k]}')             
                if v1l[k] > 0 :
                    return 1
        elif len(v2l) > min_len:
            for k in range(i+1,len(v2l)):
                print(f'k={k}, v1l={v2l[k]}')              
                if v2l[k] > 0 :
                    return -1

        return 0

 