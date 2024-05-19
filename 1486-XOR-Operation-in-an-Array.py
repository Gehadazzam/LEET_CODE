class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        maxi = 0
        for idx in range(n):
            maxi ^= start + 2 * idx
        return maxi
