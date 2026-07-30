class Solution:

    def helper(self, n, memo):
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
            return memo[n]

    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2
        return self.helper(n, memo)

        if n <= 2:
            return n

        ans = [0] * (n + 1)
        ans[1] = 1
        ans[2] = 2
        
        for i in range(3, n + 1):
            ans[i] = ans[i - 2] + ans[i - 1]
            
        return ans[n]