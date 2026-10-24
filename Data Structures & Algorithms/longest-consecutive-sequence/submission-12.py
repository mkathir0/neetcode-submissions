class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        count=1
        maxcount=0

        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                count +=1
            
            elif nums[i+1]-nums[i]==0:
                continue
            
            else:
                maxcount=max(count,maxcount)
                count=1
        
        maxcount=max(count,maxcount)
        return maxcount