class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap={}
        l=0
        maxi=0
        r=0
        while r<len(s):
            hmap[s[r]]=hmap.get(s[r],0)+1
            while (r-l+1)-max(hmap.values())>k:
                hmap[s[l]]-=1
                l+=1
            
            if (r-l+1)-max(hmap.values())<=k:
                maxi=max(maxi,r-l+1)
                r+=1
        
        return maxi