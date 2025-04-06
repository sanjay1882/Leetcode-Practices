class Solution:
    def intToRoman(self, num: int) -> str:
        d={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        s=""
        for key,val in d.items():
            while num>=val:
                s+=key
                num-=val
            else:
                continue
        return s