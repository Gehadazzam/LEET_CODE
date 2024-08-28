class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if (num % 3 != 0):
                count += min (num % 3, 3 - (num % 3))
        return count