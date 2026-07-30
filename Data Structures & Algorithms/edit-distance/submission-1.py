class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if word1 is empty
            # return len(word2)
        
        # if word2 is empty
            # return len(word1)

        # dist[i][j] = min (dist(i - 1, j), dist(i, j - 1), dist(i - 1, j - 1)) + 1
        ans = {}

        def dist(i, j):
            if i == -1: return j + 1
            if j == -1: return i + 1

            # print(i, j)
            if (i, j) in ans: return ans[(i, j)]

            k = 1 if word1[i] != word2[j] else 0
            ans[(i, j)] = min(1 + dist(i - 1, j), 1 + dist(i, j - 1), dist(i - 1, j - 1) + k)
            return ans[(i, j)]

        v = dist(len(word1) - 1, len(word2) - 1)
        # print(ans)
        return v
