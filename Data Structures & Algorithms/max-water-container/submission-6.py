class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxcount=0
        while l<r:
            ans=(r-l)*min(heights[l],heights[r])

            maxcount=max(maxcount,ans)

            if heights[l]<heights[r]:
                l+=1
            
            elif heights[l]>heights[r]:
                r-=1
            else:
                r-=1


        return maxcount