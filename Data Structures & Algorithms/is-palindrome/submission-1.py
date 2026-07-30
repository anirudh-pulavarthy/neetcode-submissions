class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                clean.append(ch.lower())

        return clean == clean[::-1]
