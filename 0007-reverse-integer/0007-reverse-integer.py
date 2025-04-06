class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        rev=0
        x=abs(x)
        while x!=0:
            rev=rev*10+(x%10)
            x//=10

        out=sign*rev
        if out<(2**31) and out> -(2**31):
            return out
        else:
            return 0
        