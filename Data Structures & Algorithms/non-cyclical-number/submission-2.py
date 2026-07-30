class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            ans = 0
            while n:
                d = n % 10
                ans += d ** 2
                n //= 10

            return ans

        slow = fast = n
        while True:
            slow = sos(slow)
            fast = sos(sos(fast))
            if slow == 1: return True
            if slow == fast: return False
        return False