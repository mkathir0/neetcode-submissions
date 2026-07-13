class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap={}

        for i in strs:
            sorted_txt="".join(sorted(i))

            if sorted_txt not in hmap:
                hmap[sorted_txt]=[]

            if sorted_txt in hmap:
                hmap[sorted_txt].append(i)

        
        return list(hmap.values())