class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap={}
        maxi=0
        l=0

        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1
            while (r-l+1 - max(hmap.values())) >k:
                hmap[s[l]] -= 1
                l+=1
            
            if (r-l+1) - max(hmap.values()) <=k:
                maxi=max(maxi,r-l+1)
        
        return maxi