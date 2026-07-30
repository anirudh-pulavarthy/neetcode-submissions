class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        dp = [float("inf")] * (amount + 1)
        coins.sort()
        dp[0] = 0
        # for c in coins:
        #     dp[c] = 1
        
        for i in range(amount + 1):
            for c in coins:
                if i - c < 0: break

                dp[i] = min(dp[i], 1 + dp[i - c])

        # for i, v in enumerate(dp):
        #     if v < float("inf"):
        #         print(i, v)
        return dp[amount] if dp[amount] != float("inf") else -1 