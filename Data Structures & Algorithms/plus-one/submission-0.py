class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        i = len(digits) - 1
        while carry:
            if i < 0:
                digits.insert(0, 1)
                return digits
            elif digits[i] < 9:
                digits[i] += 1
                carry = False
            else:
                digits[i] = 0
                i -= 1

        return digits