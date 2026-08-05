class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap={}

        for i in strs:
            res="".join(sorted(i))

            if res not in hmap:
                hmap[res]=[]
            
            hmap[res].append(i)
        
        return list(hmap.values())