class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        hmap={"}":"{","]":"[",")":"("}

        for c in s:
            if c =="{" or c=="[" or c=="(":
                stk.append(c)
            
            else:
                if not stk:
                    return False
                
                elif stk[-1]==hmap[c]:
                    stk.pop()
                
                else:
                    return False
        
        if not stk:
            return True
        
        else:
            return False