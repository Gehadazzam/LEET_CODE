class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convertToBase(num, base):
            baseNum = []
            while num > 0:
                baseNum.append(num % base)
                num //= base
            left, right = 0, len(baseNum) - 1
            while left < right:
                if baseNum[left] != baseNum[right]:
                    return False
                left += 1
                right -= 1
            return True

        for base in range(2, n - 1):
            if not convertToBase(n, base):
                return False
        return True
