class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        maxL = 1
        i, j = 0, 1
        while j < len(s):
            if s[i] == s[j]: 
                i, j = i + 1, j + 1
            else:
                # starting at j - 1, search the current substring for s[j]
                left = j - 1
                while (left >= i) and s[left] != s[j]:
                    left -= 1

                # length of current substring
                current = j - left
                maxL = max(maxL, current)

                if left == i - 1: 
                    # s[j] has never occured in the current substring so far
                    # it is a new character, proceed to the next char
                    j += 1
                else:
                    # s[j] has occured before
                    # start a new unique substring string
                    i, j = left + 1, j + 1

        return maxL