class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while l<r:
            if not s[l].isalnum():
                l+=1
            
            elif not s[r].isalnum():
                r-=1

            if s[l].isalnum() and s[r].isalnum():
                left=s[l].lower()
                right=s[r].lower()
                if left==right:
                    l+=1
                    r-=1
                else:
                    return False

            
        
        return True


                    
                

