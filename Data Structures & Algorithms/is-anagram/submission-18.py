class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap1={}

        for i in s:
            hmap1[i]=hmap1.get(i,0)+1
        
        for i in t:
            hmap1[i]=hmap1.get(i,0)-1

        for i in hmap1.values():
            if i>0:
                return False
        
        return True