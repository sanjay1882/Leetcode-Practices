class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        
        # if str(x)=="".join(list(reversed(str(x)))):
        #     return True
        # else:
        #     return False
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False
        