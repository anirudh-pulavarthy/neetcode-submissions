class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            ans = 0
            while n:
                d = n % 10
                ans += d ** 2
                n //= 10
            return ans

        slow = n
        fast = sos(n)
        while slow != fast:
            slow = sos(slow)
            fast = sos(sos(fast))
        return slow == 1 or fast == 1