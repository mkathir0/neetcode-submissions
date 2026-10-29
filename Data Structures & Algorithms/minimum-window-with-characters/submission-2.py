class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmap1={}
        hmap2={}
        res=""
        maxi=float("inf")
        l=0
        for i in t:
            hmap1[i]=hmap1.get(i,0)+1

        have, need = 0, len(hmap1)

        for r in range(len(s)):
            c = s[r]
            hmap2[c]=hmap2.get(c,0)+1
            if c in hmap1 and hmap2[c] == hmap1[c]:
                have += 1

            while have == need:
                if(r-l+1)<maxi:
                    maxi=(r-l+1)
                    start=l
                
                hmap2[s[l]]-=1
                if s[l] in hmap1 and hmap2[s[l]] < hmap1[s[l]]:
                    have -= 1

                if hmap2[s[l]]==0:
                    del hmap2[s[l]]
                
                l+=1

        if maxi == float("inf"):
            return ""
        res=s[start:start+maxi]
        return res