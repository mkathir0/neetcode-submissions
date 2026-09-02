class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        result=[]
        while l<r:
            temp=numbers[l]+numbers[r]
            if temp>target:
                r-=1
            elif temp<target:
                l+=1
            else:
                result.append(l+1)
                result.append(r+1)
                break
        
        return result
