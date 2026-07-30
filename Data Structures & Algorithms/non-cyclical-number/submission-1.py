class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            ans = 0
            while n:
                d = n % 10
                ans += d ** 2
                n //= 10
            
            return ans

        seen = set()
        while n not in seen:
            if n == 1: return True
            seen.add(n)
            n = sos(n)
        return False