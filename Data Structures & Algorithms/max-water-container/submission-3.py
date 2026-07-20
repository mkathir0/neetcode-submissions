class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxi=0

        while l<=r:
            ans=(r-l)*min(heights[l],heights[r])
            maxi=max(ans,maxi)
            if heights[l]<heights[r]:
                l+=1
            elif heights[r]<heights[l]:
                r-=1
            else:
                r-=1
        
        maxi=max(maxi,ans)
        return maxi