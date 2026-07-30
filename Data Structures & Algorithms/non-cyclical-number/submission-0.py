class Solution:
    def __init__(self):
        self.seen = set()

    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        if n in self.seen: return False

        def sos(n):
            ans = 0
            while n:
                d = n % 10
                ans += d ** 2
                n //= 10
            
            return ans

        self.seen.add(n)
        return self.isHappy(sos(n))