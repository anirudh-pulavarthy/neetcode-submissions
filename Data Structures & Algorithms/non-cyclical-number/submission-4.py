class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            ans = 0
            while n:
                d = n % 10
                ans += d ** 2
                n //= 10

            print(ans)
            return ans

        slow = n
        fast = sos(n)
        if slow == 1 or fast == 1: return True

        while slow != fast:
            if slow == 1 or fast == 1: return True

            slow = sos(slow)
            fast = sos(sos(fast))
        return False