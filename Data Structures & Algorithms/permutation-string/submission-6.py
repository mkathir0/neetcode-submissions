class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap1={}
        hmap2={}
        l=0
        for i in s1:
            hmap1[i]=hmap1.get(i,0)+1
        
        for r in range(len(s2)):
            hmap2[s2[r]]=hmap2.get(s2[r],0)+1

            while (r-l+1)>len(s1):
                hmap2[s2[l]]-=1

                if hmap2[s2[l]]==0:
                    del hmap2[s2[l]]
                
                l+=1
            
            if (r-l+1)==len(s1):
                if hmap1==hmap2:
                    return True

        return False