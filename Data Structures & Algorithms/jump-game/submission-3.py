class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r=0
        count=0
        while r<len(nums):
            if count<0:
                return False

            count=max(count,nums[r])
            r+=1
            count-=1
        
        return True