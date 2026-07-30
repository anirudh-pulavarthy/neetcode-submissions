class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while n:
            res += ( (2 ** (31 - i)) * (n & 1) )
            i += 1
            n = n >> 1

        return res