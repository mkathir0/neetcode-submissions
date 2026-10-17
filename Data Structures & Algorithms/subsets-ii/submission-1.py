class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        curset=[]
        nums.sort()

        def backtrack(i):
            if i>=len(nums):
                subset.append(curset.copy())
                return
            
            curset.append(nums[i])
            backtrack(i+1)
            curset.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1

            backtrack(i+1)
        
        backtrack(0)

        return subset

