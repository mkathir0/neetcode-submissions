class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        
        hmap={}

        for i in s:
            hmap[i]=hmap.get(i,0)+1
        
        for i in t:
            hmap[i]=hmap.get(i,0)-1

        for i in hmap.values():
            if i !=0:
                return False
        
        return True

        