import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        result=[]
        heap=[]
        for i in nums:
            hmap[i]=hmap.get(i,0)+1
        
        for i,n in hmap.items():
            heapq.heappush(heap,(n,i))

            if len(heap)>k:
                heapq.heappop(heap)
            
        
        while heap:
            result.append(heapq.heappop(heap)[1])

        return result