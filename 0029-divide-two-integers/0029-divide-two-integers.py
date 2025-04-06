class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        out=int(float(dividend/divisor))

        if out>(2**31-1):
            return 2**31-1
        if out<(-2**31):
            return -2**31
        return out
        