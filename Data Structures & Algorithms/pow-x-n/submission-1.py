class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        elif n == -1: return 1 / x
        
        v = self.myPow(x, n // 2)
        if n & 1:   return x * v * v
        else: return v * v