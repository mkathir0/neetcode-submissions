class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for i in nums2:
            nums1.append(i)
        

        nums1.sort()
        n=len(nums1)
        if len(nums1)%2==0:
            res1=nums1[(n//2)-1]
            res2=nums1[(n//2)]
            total=(res1+res2)/2
            return float(total)
        
        else:
            resu1=nums1[(n)//2]
            return float(resu1)