class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True

        isPalindrome = lambda someString: someString == someString[::-1]

        l, r = 0, len(s) - 1

        while l <= r:   #change later
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                string_without_l = s[l+1 : r+1]
                if isPalindrome(string_without_l):
                    # print(f"without l at {l}")
                    return True

                string_without_r = s[l : r]
                if isPalindrome(string_without_r):
                    # print(f"without r at {l}{r}, string is {string_without_r}")
                    return True

                return False

        return True
