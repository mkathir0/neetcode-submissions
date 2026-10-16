class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subset=[]
        curset=[]

        def backtrack(i):
            if i>=len(nums):
                subset.append(curset.copy())
                return
            
            curset.append(nums[i])
            backtrack(i+1)
            curset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return subset
